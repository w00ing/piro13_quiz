from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):

    user = models.OneToOneField(
        User, related_name="quizes", on_delete=models.CASCADE, blank=True
    )
    title = models.CharField(max_length=100)
    answer_1 = models.CharField(max_length=100)
    answer_2 = models.CharField(max_length=100)
    answer_3 = models.CharField(max_length=100)
    answer_4 = models.CharField(max_length=100)
    answer_5 = models.CharField(max_length=100)
    answer_6 = models.CharField(max_length=100)
    answer_7 = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)
