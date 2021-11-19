from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def my_form_post():
    meal = float(request.form["meal"])
    tip = float(request.form["tip"])
    tax = float(request.form["tax"])
    total_tip = tip / 100
    total_tax = tax / 100
    meal = meal + (meal * total_tax)
    total = round((meal + (meal * total_tip)), 2)
    return str(total)

if __name__ == "__main__":
    app.run(debug=True)

