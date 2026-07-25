from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb:27017/")
db = client["EmployeeDB"]
collection = db["employees"]

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        employee = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "department": request.form["department"]
        }

        collection.insert_one(employee)

        print("Employee Added:", employee)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
