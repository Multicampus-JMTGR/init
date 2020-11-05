from django.conf import settings
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from datetime import datetime


# 자격증 카테고리 예) 정보통신
class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True) #PK(카테고리PK)
    name = models.CharField(max_length=50) #카테고리 이름
    
    class Meta:
        db_table = 'CATEGORY'

    def __str__(self):
        return self.name

class Certificate(models.Model):
    cert_id = models.IntegerField(primary_key=True) #PK(자격증PK)
    cat_id = models.ForeignKey(Category, related_name="certificates", on_delete=models.CASCADE) #FK(카테고리PK)
    name = models.CharField(max_length=100) #자격증 이름
    department = models.CharField(max_length=100) #시행기관
    pass_percent = models.FloatField(max_length=50) #합격률
    cost = models.CharField(max_length=500) #응시료

    class Meta:
        db_table = "CERTIFICATE"

    def __str__(self):
        return self.name

# 스터디 플랜
# ondelete 설명 : https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html
class StudyPlan(models.Model):
    content_id = models.AutoField(primary_key=True, default=1) #PK(스터디플랜PK)
    id_token = models.ForeignKey(User, on_delete=models.CASCADE) #FK(사용자PK)
    cert_id = models.ForeignKey(Certificate, on_delete=models.CASCADE) #FK(자격증PK)
    date = models.DateField(blank=True, null=True) #달력에서 날짜 부분
    contents = models.CharField(max_length=1000) #todolist작성내용

    class Meta:
        db_table = "STUDY_PLAN"

    def __str__(self):
        return self.contents


# 자격증 접수일정 정보
class CertSchedule(models.Model):
    # schedule_id = models.AutoField()
    cert_id = models.ForeignKey(Certificate, on_delete=models.CASCADE) #FK(자격증PK)
    test_round = models.IntegerField() #회차(숫자?)
    test_type = models.CharField(max_length=10) #필기/실기
    reg_start_date = models.DateField(blank=True, null=True) #접수 시작 날짜
    reg_end_date = models.DateField(blank=True, null=True) #접수 마감 날짜
    test_start_date = models.DateField(blank=True, null=True) #시험 시작 날짜
    test_end_date = models.DateField(blank=True, null=True) #시험 마감 날짜
    result_date_1 = models.DateField(blank=True, null=True) #결과 날짜
    result_date_2 = models.DateField(blank=True, null=True) #추가적인 결과 날짜가 있으면
    
    class Meta:
        db_table = "CERT_SCHEDULE"
        # 장고에서는 compound PK 지정이 안되서 pk는 자동생성되는 인덱스 값을 만들고 유니크한 필드값을 지정
        unique_together = ['cert_id', 'test_round', 'test_type'] 

    def __str__(self):
        return self.cert_id

# 관심 자격증 표시 여부
# ondelete 설명 : https://lee-seul.github.io/django/backend/2018/01/28/django-model-on-delete.html
# class CertLikes:
#     # FK두개 합쳐 하나의 PK를 이룸
#     id_token = models.ForeignKey(User, on_delete=models.CASCADE) #FK(사용자PK)
#     cert_id = models.ForeignKey(Certificate, on_delete=models.CASCADE) #FK(자격증PK)

#     class Meta:
#         db_table = "CERTLIKES"

# class CatLikes:
#     # FK두개 합쳐 하나의 PK를 이룸
#     id_token = models.ForeignKey(User, on_delete=models.CASCADE) #FK(사용자PK)
#     cat_id = models.ForeignKey(Category, on_delete=models.CASCADE) #FK(카테고리PK)
    

#     class Meta:
#         db_table = "CATLIKES"
