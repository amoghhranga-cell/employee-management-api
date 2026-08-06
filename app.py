from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Employee Data
employees = [
    {
        "id": 1,
        "name": "Amogh",
        "department": "DevOps",
        "email": "amogh@example.com"
    }
]

# Home API
@app.route("/")
def home():
    return jsonify({
        "message": "Employee Management API is Running!"
    })

# Get All Employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# Add a New Employee
@app.route("/employees", methods=["POST"])
def add_employee():

    new_employee = request.get_json()

    employees.append(new_employee)

    return jsonify({
        "message": "Employee added successfully",
        "employee": new_employee
    }), 201


if __name__ == "__main__":
    app.run(debug=True)