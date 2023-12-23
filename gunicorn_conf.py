# 定义同时开启的处理请求的进程数量，根据网站流量适当调整
workers = 5
# 采用gevent库，支持异步处理请求，提高吞吐量
worker_class = "gevent"
# 这里5000可以随便调整
bind = "127.0.0.1:5000"
# 错误日志文件的路径
errorlog = "/data/log/gunicorn_error.log"
# 访问日志文件的路径
accesslog = "/data/log/gunicorn_access.log"
# 日志级别
loglevel = "debug"
# 超时时间
timeout = 600
# 设置gunicorn访问日志格式，错误日志无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# 监听队列
backlog = 512

