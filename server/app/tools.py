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
    # 保存文件相关逻辑，根据使用的平台进行修改
    # 比如如果接入阿里云腾讯云之类的对象存储，可以把下面的代码替换
    # 传入参数：flank_file_obj
    # flank_file_obj flask获取到的文件对象
    # 返回参数： { "url": url, "key": filekeykey }
    # url 返回上传后的url路径，本地上传可能为相对路径
    # filekey 返回对应平台的文件标识符之类的东西，用于后续对文件的操作
    # 这里的实现是：本地

    from .config import UPLODAD_FILE_SAVE

    fileext = os.path.splitext(flank_file_obj.filename)[-1]
    filename = get_filename() + fileext

    filepath = os.path.join(UPLODAD_FILE_SAVE, filename)

    flank_file_obj.save(filepath)

    url = "/upload/" + filename

    return { "url": url, "key": filename }

def del_file(filekey) -> bool:
    # 删除文件相关逻辑，根据使用的平台进行修改
    # 比如如果接入阿里云腾讯云之类的对象存储，可以把下面的代码替换
    # 传入参数：filekey
    # filekey 传入对应平台的文件标识符之类的东西，用于删除文件
    # 返回参数： isDel -> bool
    # isDel 是否删除成功
    # 这里的实现是：本地

    from .config import UPLODAD_FILE_SAVE

    filepath = os.path.join(UPLODAD_FILE_SAVE, filekey)

    if os.path.isfile(filepath):
        os.remove(filepath)
        return True
    else:
        return False 

