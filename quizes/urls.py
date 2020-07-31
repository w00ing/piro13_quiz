from django.urls import path
from .views import QuizList, RankingList

app_name = "quizes"

urlpatterns = {
    path('list/', QuizList.as_view()),
    path('ranking/', RankingList.as_view()),
}
