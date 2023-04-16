from django.http import HttpResponse
import hashlib
from project.settings import SALT,JWTHEADER
from . import models
 
def hash_code(s, salt=None):  # 加点盐
    if not salt:
        salt = SALT
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

#注册 https://www.cnblogs.com/marvin-wen/articles/13062871.html
def register(request):
    if request.method != "POST":
        return HttpResponse("400 请使用POST请求")

    username = request.POST.get("username")
    password = request.POST.get("password")
    confirm = request.POST.get("confirm")

    if username=="" or password=="" or confirm=="":
        return HttpResponse("400 请检查填写的内容！")

    if password != password:  # 判断两次密码是否相同
        return HttpResponse("400 两次输入的密码不同！")
    
    if models.User.objects.filter(username=username):  # 用户名重名
        return HttpResponse("400 用户名已经存在！")

    # 创建新用户
    new_user = models.User.objects.create()
    new_user.username = username
    new_user.password = hash_code(password)  # 使用加密点盐密码
    new_user.save()
    
    return HttpResponse("200 注册成功！")

#登录
def login(request):
    if request.method != "POST":    #是否POST请求
        return HttpResponse("400 请使用POST请求")

    #获取数据
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username=="" or password=="":    #内容
        return HttpResponse("400 请检查填写的内容！")
    
    try:
        #查询数据库
        hash_password = hash_code(password)
        user = models.User.objects.get(username=username, password=hash_password)
        #登录 https://juejin.cn/post/7074597294066597925
        #jwt载荷
        payload = {
            'id': user.id,
            'username': user.username,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1) # exp 为有效时间，表示token的有效时间
        }
        
        result = jwt.encode( #形成token
            headers=JWTHEADER, # 传入headers以及payloads进行加密
            payload=payload,
            key=settings.SECRET_KEY,    # salt为加密,他将会与第一部分+第二部分一起进行加密，这里salt的值为settings文件里的SECRET_KEY
            algorithm=JWTHEADER["alg"],  # algorithm将传入加密方式
        ).decode('utf-8')
        
        """最终返回登录成功的信息以及token """
        return HttpResponse("200 登录成功 "+result)
    except:
        return HttpResponse("400 用户名或密码不正确！")