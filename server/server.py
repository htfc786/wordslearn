from config import * # 导入config
from db import *
from flask import Flask

app = Flask(__name__)

app.secret_key = SECRET

@app.route('/')
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=PORT, 
        debug=DEBUG, 
    )