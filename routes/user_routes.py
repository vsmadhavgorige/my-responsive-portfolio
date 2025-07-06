from flask import Blueprint,jsonify

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/home_section/<int:user_id>",methods=["GET"])
def home_section(user_id):
    try:
        return jsonify({"message": "api is working"}),200
    except :
        pass