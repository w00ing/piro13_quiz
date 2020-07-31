from django.db import models

#2. 퀴즈 목록 페이지
class Quiz(models.Model):
    user = models.TextField()  #로그인한 사람
    title = models.TextField()  #퀴즈 제목
    person = models.TextField()  #출제자

    def __str__(self):
        return self.user


#5. 퀴즈 랭킹 확인 페이지
class Ranking(models.Model):
    name = models.CharField(max_length=255)  #퀴즈를 푼 사람 이름
    number = models.IntegerField()  #퀴즈 문제 맞춘 개수

    def __str__(self):
        return self.name