
from . import app
from . import Users

@app.route('/user')
def hellouser():
    Users()
    return 'hello'