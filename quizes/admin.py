from django.contrib import admin
from . import models


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):

    """ Quiz Admin Definition """

    pass
