from django.urls import path
from .views import QuizList

app_name = "quizes"

urlpatterns = {
    path('', QuizList.as_view())
}
