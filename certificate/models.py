from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# 자격증 카테고리 예) 정보통신
class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True) #PK(카테고리PK)
    name = models.CharField(max_length=50) #카테고리 이름
    
    class Meta:
        db_table = 'CATEGORY'

    def __str__(self):
        return self.name

# 자격증 예) 정보처리기사
class Certificate(models.Model):
    cert_id = models.IntegerField(primary_key=True) #PK(자격증PK)
    cat_id = models.ForeignKey(Category, related_name="certificates", on_delete=models.CASCADE) #FK(카테고리PK)
    name = models.CharField(max_length=100) #자격증 이름
    department = models.CharField(max_length=100) #시행기관
    pass_percent = models.FloatField(max_length=50, blank=True, null=True) #합격률
    pass_percent_sil = models.FloatField(max_length=50, blank=True, null=True) #합격률
    cost = models.CharField(max_length=500, blank=True, null=True) #응시료
    cost_sil = models.CharField(max_length=500, blank=True, null=True) #응시료
    examinee = models.IntegerField(default=0, blank=True, null=True) #응시자 수
    examinee_sil = models.IntegerField(default=0, blank=True, null=True) #응시자 수
    link = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = "CERTIFICATE"

    def __str__(self):
        return self.name



# 자격증 접수일정 정보
class CertSchedule(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    cert_id = models.ForeignKey(Certificate, related_name="cert_schedule", on_delete=models.CASCADE) #FK(자격증PK)
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
