from flask import jsonify 
from api.manage import Employee
from main import user_bp

users_list = [
                {"name":"Hari" , "age" : 20 },
                {"name":"Venkatesh" , "age" : 30 },
                {"name":"HV" , "age" : 40 },
            ]


# user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["get"])
def get_users_list():
    return jsonify(users_list)

@user_bp.route("/", methods=["post"])
def get_users_list():
    try:
        print("Adding User")
        user = Employee(
                id=1,
                name = 'Hari',
                role = 'Developer',
                experience = 1,
                reporting = 'Kumar',
                joined_at = '2017-01-01'
                )
        user.add()
        return "User Added"
    except Exception as err:
        return "error"        