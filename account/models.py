from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) #계정 생성 시점 auto_now_add로 필드 추가시점 기록
    updated_at = models.DateTimeField(auto_now=True) #계정 업데이트 시점 auto_now로 필드 업데이트 기록


    class Meta:
        db_table = 'accounts' #이름 설정하지 않아도 되는데, 이상한 값으로 기록될 수 있으니 설정함.