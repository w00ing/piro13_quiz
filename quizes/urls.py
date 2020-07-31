from django.urls import path
from . import views

app_name = "quizes"

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('quiz/<int:question_id>/', views.quiz, name='quiz'),
    path('detail<int:question_id>/', views.detail, name='detail'),
]

