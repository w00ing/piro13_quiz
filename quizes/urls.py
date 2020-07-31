from django.urls import path
from . import views


app_name = "quizes"

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz/create/", views.make_quiz, name="make-quiz"),
    path("users/<int:pk>", views.solve_quiz, name="solve-quiz"),
    path('list/', views.QuizList.as_view()),
    path('ranking/', views.RankingList.as_view()),
]

