from django.views.generic.list import ListView
from .models import Quiz, Ranking

#2. 퀴즈 목록 화면---------------------------------------------------
class QuizList(ListView):
    model = Quiz
    template_name = 'list.html'

#5. 퀴즈 랭킹 화면---------------------------------------------------
class RankingList(ListView):
    model = Ranking
    rank = Ranking.objects.all().order_by('-number')
    template_name = 'ranking.html'


