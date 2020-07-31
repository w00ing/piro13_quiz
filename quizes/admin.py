from django.contrib import admin
from . import models
from .models import Question


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):

    """ Quiz Admin Definition """

    pass


admin.site.register(Question)
