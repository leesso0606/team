from django.db import models
# 아직 데이터 베이스 안만듬
# Create your models here.

class Brand(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', '커피'),
        ('chicken', '치킨'),
        ('hair', '미용실'),
        ('convenience', '편의점'),
    ]

    name = models.CharField(max_length=100) #브랜드 이름
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )
    homepage = models.URLField(blank=True) # 프렌차이즈 공식 홈페이지 주소
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
