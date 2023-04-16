from django.db import models

# Create your models here.

class User(models.Model):
    
    id = models.IntegerField(verbose_name="用户id", db_index=True, primary_key=True)
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=256, verbose_name="密码-可SHA256")
    slat = models.CharField(max_length=32, verbose_name="密码加盐")
    avatar = models.CharField(max_length=1024, verbose_name="头像URL")
    sign = models.CharField(max_length=128, verbose_name="用户个人签名")
    created_time = models.DateTimeField(max_length=128, auto_now_add=True, verbose_name="注册时间")
    is_admin = models.BooleanField(default=False, verbose_name="是否管理员")
    is_del = models.BooleanField(default=False, verbose_name="是否删除")
    
    class Mate:
        db_table = "users"