from django.db import models

class Quiz(models.Model):
    user = models.TextField()
    title = models.TextField()
    person = models.TextField()

    def __str__(self):
        return self.user


#5.퀴즈 랭킹 확인 페이지
#class Ranking(models.Model):
#    name = models.CharField(max_length=255) #퀴즈를 푼 사람 이름
#    number = models.IntegerField()  #퀴즈 문제 맞춘 개수