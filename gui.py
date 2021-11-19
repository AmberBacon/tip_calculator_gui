from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def my_form():
    return render_template("test.html")
    
@app.route("/", methods=["POST"])
def my_form_post():
    #global tip
    #global meal
    #global tax
    #global total 
    meal = float(request.form["meal"])
    tip = float(request.form["tip"])
    tax = float(request.form["tax"])
    total_tip = tip / 100
    total_tax = tax / 100
    meal = meal + (meal * total_tax)
    total = round((meal + (meal * total_tip)), 2)
    return str("The total of your bill including tax and tip is " + str(total))
        
if __name__ == "__main__":
    app.run(debug=False)

