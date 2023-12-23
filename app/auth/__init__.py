from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import sign_up, login, send_verify_code, confirm_verify_code, change_password

