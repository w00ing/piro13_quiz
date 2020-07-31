from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):

    user = models.OneToOneField(
        User, related_name="quiz", on_delete=models.CASCADE, blank=True
    )
    title = models.CharField(max_length=100, null=True)
    answer_1 = models.CharField(max_length=100, null=True)
    answer_2 = models.CharField(max_length=100, null=True)
    answer_3 = models.CharField(max_length=100, null=True)
    answer_4 = models.CharField(max_length=100, null=True)
    answer_5 = models.CharField(max_length=100, null=True)
    answer_6 = models.CharField(max_length=100, null=True)
    answer_7 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.title)

#5. 퀴즈 랭킹 확인 페이지
class Ranking(models.Model):
    name = models.CharField(max_length=255)  #퀴즈를 푼 사람 이름
    number = models.IntegerField()  #퀴즈 문제 맞춘 개수

    def __str__(self):
        return self.name

