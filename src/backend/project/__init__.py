import pymysql
pymysql.version_info = (1, 4, 13, "final", 0) #解决报错 https://cloud.tencent.com/developer/article/1755110
pymysql.install_as_MySQLdb() 