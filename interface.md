## 说明

- 域名：api.baiwow.com
- 请求方式：POST

## 注册

### 地址
```
http://域名/sign_up
```
### 请求
```json
{
    "email":"xxx",
    "password":"xxx",
    "name":"xxx"
}
```
### 响应
```json
{
   "code": 0,
   "msg": "success"
}
```
### 其他错误码
|  错误码   | 含义  |
|  ----  | ----  |
| 10001  | email exist |

## 登录

### 地址
```
http://域名/login
```
### 请求
```json
{
    "email":"99_test@qq.com",
    "password":"99_password"
}
```
### 响应
```json
{
    "code":0,
    "data":{
        "name":"99_name",
        "token":"c62f83b5385ab1ec2f"
    },
    "msg":"success"
}
```
### 其他错误码
|  错误码   | 含义  |
|  ----  | ----  |
| 10002  | email not exist or password not right |

## 发送验证码

### 地址
```
http://域名/send_verify_code
```
### 请求
```json
{
    "email":"5_test@qq.com"
}
```
### 响应
```json
{
    "code": 0,
    "msg": "success"
}
```
### 其他错误码
|  错误码   | 含义  |
|  ----  | ----  |
| 10003  | email not exist |

## 确认验证码

### 地址
```
http://域名/confirm_verify_code
```
### 请求
```json
{
    "email":"5_test@qq.com",
    "verify_code":"1234"
}
```
### 响应
```json
{
    "code": 0,
    "data": {
        "verify_token": "c62f83b5385ab1ec2f1e14e"
    },
    "msg": "success"
}
```
### 其他错误码
| 错误码   | 含义  |
|-------| ----  |
| 10004 | email verify_code not exist |
| 10005 | verify_code not right |

## 修改密码

### 地址
```
http://域名/change_password
```
### 请求
```json
{
    "verify_token":"839fe5ed5a9b0f37e1e627",
    "new_password":"5_password"
}
```
### 响应
```json
{
    "code": 0,
    "msg": "success"
}
```
### 其他错误码
| 错误码   | 含义  |
|-------| ----  |
| 10006 | verify_token is not right |
| 10007 | user_id not exist |

