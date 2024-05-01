from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        expression = request.form["num1"]+request.form["operator"]+request.form["num2"]
        result = eval(expression)
        print(result)
        return render_template("calculator.html", result1=result)
    return render_template("calculator.html")

if __name__ == "__main__":
    app.run("0.0.0.0")