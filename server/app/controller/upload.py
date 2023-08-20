from flask import send_file, abort
import os

from . import app
from ..config import UPLODAD_FILE_SAVE

@app.route('/upload/<subfile>', methods=['GET'])
def upload(subfile=''):
    print(subfile)
    filepath = os.path.join(UPLODAD_FILE_SAVE, subfile)
    if os.path.isfile(filepath):
        return send_file(filepath)
    # 没有文件
    abort(404) 
    return "",404
