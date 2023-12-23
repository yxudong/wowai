from flask import jsonify, request
from . import auth
from ..util import *


@auth.route('/change_password', methods=['POST'])
def ChangePassword():
    req = request.json
    print("req: ", req)

    verify_token = req.get("verify_token", "")
    print("verify_token: ", verify_token)
    new_password = req.get("new_password", "")
    print("new_password: ", new_password)

    # 解密 verify_token 获取 user_id
    user_id = get_user_id_from_token(verify_token)
    print("user_id: ", user_id)
    if not user_id:
        code = 10006
        resp = {
            "code": code,
            "msg": "verify_token is not right",
        }
        return jsonify(resp)

    # 校验 user_id 是否存在
    db = connect_sql()
    check_sql = "SELECT user_id FROM user_info WHERE user_id = '{}'".format(user_id)
    print("check_sql: ", check_sql)
    result = sql_select(db, check_sql)
    if len(result) == 0:
        code = 10007
        resp = {
            'code': code,
            'msg': "user_id not exist"
        }
        return jsonify(resp)

    update(db, new_password, user_id)
    code = 0
    resp = {
        "code": code,
        "msg": "success",
    }
    return jsonify(resp)


def update(db, password, user_id):
    cursor = db.cursor()
    sql = "update user_info set password = %s WHERE user_id = %s"
    print("update_sql: ", sql)
    cursor.execute(sql, (password, user_id))
    db.commit()
    return
