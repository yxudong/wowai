import random
import requests


HOST = "localhost:5000"


# 1. 注册
def test_SignUp():
    # post 请求
    url = "http://{}/sign_up".format(HOST)
    i = random.randint(0, 10)
    i = 99
    req = {
        "email": "{}_test@qq.com".format(i),
        "password": "{}_password".format(i),
        "name": "{}_name".format(i)
    }
    # req = {"data": data}
    print(req)
    r = requests.post(url, json=req)
    print(r.text)


# 2. 登录
def test_Login():
    # post 请求
    url = "http://{}/login".format(HOST)
    req = {"email": "99_test@qq.com", "password": "99_password"}  # true
    # req = {"email": "5_test@qq.com", "password": "5_password"}  # false
    r = requests.post(url, json=req)
    print(r.text)


# 3. send verify_code
def test_SendVerifyCode():
    # post 请求
    url = "http://{}/send_verify_code".format(HOST)
    req = {"email": "99_test@qq.com"}  # true
    # req = {"email": "0_test@qq.com", "password": "1_password"}#false
    r = requests.post(url, json=req)
    print(r.text)


# 4. 验证 verify_code
def test_ConfirmVerifyCode():
    # post 请求
    url = "http://{}/confirm_verify_code".format(HOST)
    req = {"email": "99_test@qq.com", "verify_code": "1234"}  # true
    # req = {"email": "5_test@qq.com", "verify_code": "1235"}  # false
    # req = {"email": "4_test@qq.com", "verify_code": "1234"}  # false
    r = requests.post(url, json=req)
    print(r.text)


# 5. 更改 password
def test_ChangePassword():
    # post 请求
    url = "http://{}/change_password".format(HOST)
    req = {"verify_token": "c62f83b5385ab1ec2f1e14e7f1df449c27b1d0f4dec25d6293583b20afcc2f85", "new_password": "99_password"}  # true
    # req = {"verify_token": "dhudhusgdusgdyy7627327", "new_password": "3333"}  # false
    r = requests.post(url, json=req)
    print(r.text)


if __name__ == '__main__':
    # test_SignUp()
    # test_Login()
    # test_SendVerifyCode()
    # test_ConfirmVerifyCode()
    test_ChangePassword()
