from django.urls import path
from . import views


app_name = "quizes"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.make_quiz, name="make-quiz"),
    path("<int:pk>/solve/", views.solve_quiz, name="solve-quiz"),
    path("list/", views.quiz_list, name="list"),
    path("<int:pk>/ranking/", views.quiz_ranking, name="ranking")
    # path('', views.home, name='home'),
    # path('list/', views.list, name='list'),
    # path('create/', views.create, name='create'),
    # path('quiz/<int:question_id>/', views.quiz, name='quiz'),
    # path('detail<int:question_id>/', views.detail, name='detail'),
]

