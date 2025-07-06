from flask import Blueprint,jsonify
from utils.logger import log
from utils.db_utils import db

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/home_section/<int:user_id>",methods=["GET"])
def home_section(user_id):
    try:
        1 / 0
    except  Exception as e:
        log.error(e)
        return jsonify({
            "error": "Please contact adminatrator or try again some aftersome"
        }), 500