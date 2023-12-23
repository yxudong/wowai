from flask import jsonify, request
from . import auth
from ..util import *
import random


@auth.route('/send_verify_code', methods=['POST'])
def SendVerifyCode():
    req = request.json
    print("req: ", req)

    email = req.get("email", "")
    print("email: ", email)

    db = connect_sql()
    check_sql = "SELECT user_id FROM user_info WHERE email = '{}'".format(email)
    print("check_sql: ", check_sql)
    result = sql_select(db, check_sql)

    if len(result) == 0:
        code = 10003
        resp = {
            'code': code,
            'msg': "email not exist"
        }
        return jsonify(resp)

    user_id = result[0][0]
    print("user_id", user_id)

    check_sql = "select verify_code from user_verify_code where email = '{}'".format(email)
    print("check_sql: ", check_sql)
    result = sql_select(db, check_sql)
    verify_code = '%04d' % random.randint(0, 9999)  # 生成验证码
    # TODO 测试后删除
    verify_code = "1234"
    verify_code = str(verify_code)
    print("verify_code: ", verify_code)
    if len(result) == 0:
        id = generate_id()
        insert(db, id, user_id, email, verify_code)
    else:
        update(db, verify_code, user_id)

    # todo 发送邮件
    # receivers = ['yangguixiu18@gmail.com']  # 测试接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # code = send_email(verify_code, receivers)

    code = 0
    resp = {
        "code": code,
        "msg": "success",
    }
    return jsonify(resp)


def insert(db, id, user_id, email, verify_code):
    cursor = db.cursor()
    sql = """INSERT INTO user_verify_code(id,user_id,email, verify_code) VALUES (%s,%s,%s,%s)"""
    print("INSERT", sql)
    cursor.execute(sql, (id, user_id, email, verify_code))
    db.commit()
    return


def update(db, verify_code, user_id):
    cursor = db.cursor()
    sql = "update user_verify_code set verify_code= %s where user_id=%s"
    print("update_sql: ", sql)
    cursor.execute(sql, (verify_code, user_id))
    db.commit()
    return
