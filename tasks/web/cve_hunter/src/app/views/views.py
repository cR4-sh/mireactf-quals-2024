from flask import Blueprint, render_template, request, session, redirect, abort, \
    url_for
from app.db import db
from loader import SECRET_CODE


common_blueprint = Blueprint('common', __name__, template_folder='app/templates')


@common_blueprint.route('/')
def index():
    is_authenticated = 'username' in session
    return render_template('start_page.html', is_authenticated=is_authenticated)


@common_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if 'username' in session:
        return redirect('/profile')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        authenticated, user = db.authenticate_user(username, password)

        if authenticated:
            session['username'] = user['username']
            session['email'] = user['email']
            return redirect('/profile')
        else:
            error = 'Неверный логин или пароль'
    return render_template('login.html', error=error)


@common_blueprint.route('/check_code', methods=['GET'])
def check_code():
    cve_id = request.args.get('cve_id')
    error = request.args.get('error', '')
    if cve_id:
        return render_template('check_code.html', cve_id=cve_id, error=error)
    else:
        return redirect('/search')


@common_blueprint.route('/exploit', methods=['POST'])
def exploit():
    cve_id = request.form.get('cve_id')
    input_code = request.form.get('code')
    if input_code == SECRET_CODE:
        cve = db.search_cve(cve_id)
        if cve:
            return render_template('exploit.html', cve=cve)
        else:
            return redirect(url_for('common.check_code', cve_id=cve_id, error='CVE не найдено'))
    else:
        return redirect(url_for('common.check_code', cve_id=cve_id, error='Неверный код! Продукт находится на этапе закрытого тестирования и в текущий момент только admin имеет доступ к секретному коду.'))


@common_blueprint.route('/profile')
def profile():
    if 'username' in session:
        return render_template("profile.html",  username=session['username'], email=session['email'], is_authenticated=True)
    else:
        return redirect('/login')


@common_blueprint.route('/search', methods=['GET'])
def search():
    cve_id = request.args.get('cve_id')
    if cve_id:
        cve = db.search_cve(cve_id)
        if cve:
            return render_template('search.html', cves=[cve], request=request)
        else:
            return render_template('search.html', cves=[], request=request)
    else:
        cves = db.get_all_cves()
        return render_template('search.html', cves=cves, request=request)


@common_blueprint.route('/search', methods=['POST'])
def search_exploit():
    cve_id = request.form['cve_id']
    cve = db.search_cve(cve_id)
    if cve:
        return cve['exploit']
    else:
        return 'CVE не найдено', 404


@common_blueprint.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return render_template('start_page.html', is_authenticated=False)


@common_blueprint.route('/verify_2fa', methods=['POST'])
def verify_2fa():
    if 'username' in session and session['username'] == 'admin':
        input_2fa_code = request.form['secretPassword']
        if db.verify_2fa(session['username'], input_2fa_code):
            return render_template('secret_code.html', flag=SECRET_CODE)
        else:
            return render_template('profile.html', username=session['username'], email=session['email'], error='Неверный 2FA пароль')
    else:
        return abort(403)

