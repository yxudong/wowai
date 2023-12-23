from flask import jsonify, request
from . import auth
from ..util import *


@auth.route('/login', methods=['POST'])
def Login():
    req = request.json
    print("req: ", req)

    email = req.get("email", "")
    print("email: ", email)
    password = req.get("password", "")
    print("password: ", password)

    db = connect_sql()
    check_sql = "SELECT user_id, name FROM user_info WHERE email = '{}' and password = '{}'".format(email, password)
    print("check_sql: ", check_sql)
    result = sql_select(db, check_sql)

    if len(result) == 0:
        code = 10002
        resp = {
            'code': code,
            'msg': "email not exist or password not right"
        }
        return jsonify(resp)

    user_id = result[0][0]
    print("user_id", user_id)
    nowtime = int(time.time())
    string = "{}_{}".format(user_id, nowtime)
    print("string", string)
    token = str(des_encrypt(string), "utf-8")
    print("token", token)
    name = result[0][1]
    code = 0
    resp = {
        "code": code,
        "msg": "success",
        "data": {
            "token": token,
            "name": name
        }
    }
    return jsonify(resp)
