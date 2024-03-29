# 链接：https://juejin.cn/post/7027812466553782285
# 链接：https://blog.csdn.net/DeskyAki/article/details/89341262

from flask import Blueprint
from ..db import *
from ..tools import *

from ..config import OPEN_FILE_SERVER

app = Blueprint("controller", __name__)

from . import user, wordsadmin

if OPEN_FILE_SERVER:
    from . import upload
