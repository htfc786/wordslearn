import hashlib
import string
import random


def created_salt():
    """
    生成盐
    https://blog.csdn.net/u014333371/article/details/87084772
    """
    return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, random.randint(4,6)))

def salt_password(password, salt):
    """
    密码加盐
    password:原密码 salt:加盐
    https://blog.csdn.net/weixin_42582241/article/details/128949353
    """
    md_sale=hashlib.md5((str(password).join(salt)).encode()) # MD5加盐加密方法一：将盐拼接在原密码后
    md5salepwd=md_sale.hexdigest()
    return md5salepwd