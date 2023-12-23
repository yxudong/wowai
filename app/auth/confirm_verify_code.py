from flask import jsonify, request
from . import auth
from ..util import *


@auth.route('/confirm_verify_code', methods=['POST'])
def ConfirmVerifyCode():
    req = request.json
    print("req: ", req)

    email = req.get("email", "")
    print("email: ", email)
    verify_code = req.get("verify_code", "")
    print("verify_code: ", verify_code)

    db = connect_sql()
    check_sql = "SELECT verify_code,user_id FROM user_verify_code WHERE email = '{}'".format(email)
    print("check_sql: ", check_sql)
    result = sql_select(db, check_sql)
    if len(result) == 0:
        code = 10004
        resp = {
            'code': code,
            'msg': "email verify_code not exist"
        }
        return jsonify(resp)

    verify_code_save = result[0][0]
    user_id = result[0][1]
    string = "{}_{}".format(user_id, int(time.time()))
    verify_token = str(des_encrypt(string), "utf-8")
    print("verify_token", verify_token)
    if str(verify_code_save) != str(verify_code):
        code = 10005
        resp = {
            'code': code,
            'msg': "verify_code not right"
        }
        return jsonify(resp)
    code = 0
    resp = {
        "code": code,
        "msg": "success",
        "data": {
            "verify_token": verify_token
        }
    }
    return jsonify(resp)
