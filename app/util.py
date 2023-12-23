import pymysql
import time


def connect_sql():
    # 打开数据库连接
    # 内网地址：rm-8vb8lw7mfkwmjj89w.mysql.zhangbei.rds.aliyuncs.com
    # 外网地址：rm-8vb8lw7mfkwmjj89wco.mysql.zhangbei.rds.aliyuncs.com
    db = pymysql.connect(host='rm-8vb8lw7mfkwmjj89wco.mysql.zhangbei.rds.aliyuncs.com',  # 外网地址
                         user='yangxudong',
                         password='18352839189yxD',
                         database='test_db')
    return db


def sql_select(db, sql):
    print("select: ", sql)
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    print("sql_select result: ", results)
    return results


def send_email(verify_code, receivers=None):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1307746128@qq.com"  # 用户名
    mail_pass = "aryxmqfvrttzjggd"  # 口令
    sender = "1307746128@qq.com"
    mail_title = "verify code"  # 邮件标题
    mail_content = "您的验证码为{}".format(verify_code)  # 邮件正文内容
    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender
    # msg["To"] = Header("测试邮箱",'utf-8')
    msg['To'] = ";".join(receivers)
    # 邮件正文内容
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)

        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        smtpObj.quit()
        return {"code": 0}
    except smtplib.SMTPException as e:
        print(e)
        return {"code": -1}


# 每一部分占用的位数
TIMESTAMP_BIT = 41  # 时间戳占用位数
MACHINE_BIT = 5  # 机器标识占用的位数
DATACENTER_BIT = 5  # 数据中心占用的位数
SEQUENCE_BIT = 12  # 序列号占用的位数

# 每一部分的最大值
MAX_DATACENTER_NUM = -1 ^ (-1 << DATACENTER_BIT)
MAX_MACHINE_NUM = -1 ^ (-1 << MACHINE_BIT)
MAX_SEQUENCE = -1 ^ (-1 << SEQUENCE_BIT)

# 每一部分向左的位移
MACHINE_LEFT = SEQUENCE_BIT
DATACENTER_LEFT = MACHINE_BIT + SEQUENCE_BIT
TIMESTAMP_LEFT = DATACENTER_LEFT + DATACENTER_BIT


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@singleton
class SnowFlake:
    class OverflowError(TypeError):
        """
        分布式ID生成算法占位符溢出异常，会导致生成ID为负数
        """
        pass

    class RuntimeError(TypeError):
        """
        运行时间错误，在此项目中当前运行时间小于上一次运行时间。
        """
        pass

    def __init__(self):
        if TIMESTAMP_BIT + SEQUENCE_BIT + MACHINE_BIT + DATACENTER_BIT != 63:
            raise self.OverflowError(
                "TIMESTAMP_BIT + SEQUENCE_BIT + MACHINE_BIT + DATACENTER_BIT not equal to 63bit")
        self.datacenter_id = 0  # 数据中心编号
        self.machineId = 0  # 机器标识编号
        self.sequence = 0  # 序列号
        self.last_stamp = -1  # 上一次时间戳

    def nextId(self):
        """生成下一个ID"""
        cur_stamp = self.get_new_stamp()
        if cur_stamp < self.last_stamp:
            raise self.RuntimeError(
                "Clock moved backwards. Refusing to generate id")

        if cur_stamp == self.last_stamp:
            # 相同毫秒内，序列号自增
            self.sequence = (self.sequence + 1) & MAX_SEQUENCE
            # 同一秒的序列数已经达到最大
            if self.sequence == 0:
                cur_stamp = self.get_next_mill()
        else:
            # 不同秒内，序列号为0
            self.sequence = 0

        self.last_stamp = cur_stamp
        return (cur_stamp << TIMESTAMP_LEFT) | (
                self.datacenter_id << DATACENTER_LEFT) | (
                       self.machineId << MACHINE_LEFT) | self.sequence

    def get_next_mill(self):
        mill = self.get_new_stamp()
        while mill <= self.last_stamp:
            mill = self.get_new_stamp()
        return mill

    @staticmethod
    def get_new_stamp():
        now = lambda: int(time.time() * 1000)
        return now()


def generate_id():
    s = SnowFlake()
    return s.nextId()


from pyDes import des, CBC, PAD_PKCS5
import binascii

# 秘钥
KEY = 'keiHG$93'


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY  # 密码
    iv = secret_key  # 偏移
    # secret_key:加密密钥，CBC:加密模式，iv:偏移, padmode:填充
    des_obj = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    # 返回为字节
    secret_bytes = des_obj.encrypt(s, padmode=PAD_PKCS5)
    # 返回为16进制
    return binascii.b2a_hex(secret_bytes)


def des_descrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    des_obj = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    decrypt_str = des_obj.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return decrypt_str


def get_user_id_from_token(token):
    try:
        des_str = str(des_descrypt(token), "utf-8")
        print("des_str: ", des_str)
        des_str_list = des_str.split('_')
        print("des_str_list: ", des_str_list)
        return des_str_list[0]
    except Exception as e:
        print("get_user_id_from_token error: ", e)
        print("err token: ", token)
        return None
