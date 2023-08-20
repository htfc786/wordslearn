import hashlib
import string
import random
import time
import os


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
    sha_sale = hashlib.sha256((str(password).join(salt)).encode())
    shasalepwd = sha_sale.hexdigest()
    return shasalepwd

def get_filename():
    rand = str(random.randint(100000,999999))
    nowtime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return nowtime + rand

def save_file(flank_file_obj):
    from .config import UPLODAD_FILE_SAVE

    fileext = os.path.splitext(flank_file_obj.filename)[-1]
    filename = get_filename() + fileext

    filepath = os.path.join(UPLODAD_FILE_SAVE, filename)

    flank_file_obj.save(filepath)

    return { "name": filename, "key": filename }

