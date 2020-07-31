from django.views.generic.list import ListView
from .models import Quiz

#2. 퀴즈 목록 화면---------------------------------------------------

class QuizList(ListView):
    model = Quiz
    template_name = 'list.html'




