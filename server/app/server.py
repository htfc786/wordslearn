from .config import * # 导入config
from .db import *
from .controller import app as controller

from flask import Flask

app = Flask(__name__)

# 配置数据库信息
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DBUSERNAME}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBDATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = SECRET

# 数据库
db.init_app(app)

@app.route('/')
def hello():
    return 'hello'

app.register_blueprint(controller)

def run():
    app.run(
        host="0.0.0.0", 
        port=PORT, 
        debug=DEBUG, 
    )