PORT = 8000 # 服务器运行端口
DEBUG = True # 是否使用debug模式 默认为False（不启用）
SECRET = "6prH7dY0gVNLK!kvW!4^TB1^Jv%1J^5N" # 密钥 用于加解密 建议不要使用默认这个
DBHOST = "127.0.0.1" # 数据库连接地址
DBPORT = 3306 # 数据库端口
DBUSERNAME = "root" # 数据库用户名
DBPASSWORD = "root" # 数据库密码 请改成你自己的
DBDATABASE = "wordslearn" # 数据库名称
JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24 * 7 #jwt过期时间 这里设置7天