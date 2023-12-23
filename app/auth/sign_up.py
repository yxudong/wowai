from flask import jsonify, request
from . import auth
from ..util import *


@auth.route('/sign_up', methods=['POST'])
def SignUp():
    req = request.json
    print("req: ", req)

    name = req.get("name", "")
    print("name: ", name)
    email = req.get("email", "")
    print("email: ", email)
    password = req.get("password", "")
    print("password: ", password)

    db = connect_sql()
    check_sql = "SELECT * FROM user_info WHERE email = '{}'".format(email)
    print("check_sql: ", check_sql)
    result = sql_select(db, check_sql)
    if len(result) > 0:
        code = 10001
        resp = {
            'code': code,
            'msg': "email exist"
        }
        return jsonify(resp)

    id = generate_id()
    user_id = generate_id()
    print("id: ", id)
    print("user_id: ", user_id)
    insert(db, id, user_id, name, email, password)
    code = 0
    resp = {
        'code': code,
        'msg': "success"
    }
    return jsonify(resp)


def insert(db, id, user_id, name, email, password):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 插入语句
    sql = """INSERT INTO user_info(id,user_id,
             name, email, password)
             VALUES (%s,%s,%s,%s,%s)"""
    print("insert sql: ", sql)
    # 执行sql语句
    cursor.execute(sql, (id, user_id, name, email, password))
    # 提交到数据库执行
    db.commit()
    return
