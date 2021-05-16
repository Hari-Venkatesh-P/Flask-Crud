
from api.manage import Employee
from flask import Blueprint , request , jsonify
from __init__ import app , db
import uuid
from api.utils import send_response , list_to_dict
# from api.users import user_bp

# user_bp = Blueprint("user", __name__)

# #Registering blueprints designed to the application
# app.register_blueprint(user_bp, url_prefix="/api/users")

# get all employee

@app.route('/',methods=["GET"])
def get_employees ():
    try : 
        all_employees_list = []
        all_employees = Employee.query.all()
        for emp in all_employees:
            emp_dict = emp.to_dict()
            all_employees_list.append(emp_dict)
        res = jsonify({"data": all_employees_list})
        return send_response(res, 200)
    except Exception as err:
        print(err)
        return send_response(dict(data =  "Internal Server Error"),500)


# get employee details by ID

@app.route('/<id>',methods=["GET"])
def get_employee_by_id (id):
    try:
        employee = Employee.query.filter(Employee.id == id).first()
        if employee:
            res = employee.to_dict()
        else :
            res = "No such employee"
        res = jsonify({"data": res})
        return send_response(res, 200)
    except Exception as err:
        print(err)
        return send_response(dict(data =  "Internal Server Error"),500)

# add an employee with given details

@app.route('/',methods=["POST"])
def add_employee ():
    try:
        json_obj = request.get_json()
        user = Employee(
                id= uuid.uuid4(),
                name = str(json_obj["name"]).strip(),
                role = str(json_obj["role"]).strip(),
                experience = int(json_obj["experience"]),
                reporting = str(json_obj["reporting"]).strip(),
                joined_at = str(json_obj["joined_at"]).strip()
                )
        user.add()
        return send_response(dict(data =  "User Added"),200)
    except Exception as err:
        print(err)
        return send_response(dict(data =  "Internal Server Error"),500)

# Delete an employee by given ID

@app.route('/<id>',methods=["DELETE"])
def delete_employee_by_id (id):
    try:
        Employee.query.filter(Employee.id == id).delete()
        db.session.commit()
        res = jsonify({"data": 'Employee Deleted'})
        return send_response(res, 200)
    except Exception as err:
        print(err)
        return send_response(dict(data =  "Internal Server Error"),500)    


# Updates the employee details based on given ID

@app.route('/<id>',methods=["PUT"])
def update_employee_by_id (id):
    try:
        employee = Employee.query.filter(Employee.id == id).first()
        if not employee:
            res = 'No such employee'
        else :
            json_obj = request.get_json()
            employee.role = str(json_obj["role"]).strip(),
            employee.experience = int(json_obj["experience"]),
            employee.reporting = str(json_obj["reporting"]).strip(),
            res = "Employee updated"
            db.session.commit()
        res = jsonify({"data": res})
        return send_response(res, 200)
    except Exception as err:
        print(err)
        return send_response(dict(data =  "Internal Server Error"),500)

if __name__ == "__main__":
    #To enable hot reload a, app is started in Debug mode
    app.debug = True
    app.run()