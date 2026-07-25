from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://mongodb:27017/")
db = client["EmployeeDB"]
collection = db["employees"]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        employee = {
            "full_name": request.form["fullname"],
            "father_name": request.form["fathername"],
            "qualification": request.form["qualification"],
            "mobile": request.form["mobile"],
            "email": request.form["email"],
            "address": request.form["address"]
        }

        collection.insert_one(employee)

        print("Customer Registered Successfully")
        print(employee)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
