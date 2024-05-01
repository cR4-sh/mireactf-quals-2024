from flask import Flask
from app.views.views import common_blueprint
from loader import FLASK_SECRET_KEY


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.register_blueprint(common_blueprint)
app.secret_key = FLASK_SECRET_KEY


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
