from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from quizes.models import Quiz
from django.views.generic.list import ListView
from .models import Quiz, Ranking


# Render Homepage
def home(request):
    return render(request, "base.html")


# Render Quiz Solving Page
def make_quiz(request):
    user = request.user

    if request.method == "GET":
        context = {
            "user": user,
        }
        return render(request, "quizes/make-quiz.html", context=context)

    title = request.POST.get("title", None)
    answer_1 = request.POST.get("question1", None)
    answer_2 = request.POST.get("question2", None)
    answer_3 = request.POST.get("question3", None)
    answer_4 = request.POST.get("question4", None)
    answer_5 = request.POST.get("question5", None)
    answer_6 = request.POST.get("question6", None)
    answer_7 = request.POST.get("question7", None)

    context = {
        "title": title,
        "answers": [
            answer_1,
            answer_2,
            answer_3,
            answer_4,
            answer_5,
            answer_6,
            answer_7,
        ],
    }

    Quiz.objects.create(
        title=title,
        answer_1=answer_1,
        answer_2=answer_2,
        answer_3=answer_3,
        answer_4=answer_4,
        answer_5=answer_5,
        answer_6=answer_6,
        answer_7=answer_7,
        user=request.user,
    )
    return render(request, "base.html", context=context)


def solve_quiz(request, pk):

    current_user = request.user
    quiz_owner = User.objects.get(id=pk)

    if request.method == "GET":

        context = {
            "quiz_owner": quiz_owner,
        }

        return render(request, "quizes/solve-quiz.html", context=context)

    correct_answers = [
        quiz_owner.quiz.answer_1,
        quiz_owner.quiz.answer_2,
        quiz_owner.quiz.answer_3,
        quiz_owner.quiz.answer_4,
        quiz_owner.quiz.answer_5,
        quiz_owner.quiz.answer_6,
        quiz_owner.quiz.answer_7,
    ]

    answer_1 = request.POST.get("question1", None)
    answer_2 = request.POST.get("question2", None)
    answer_3 = request.POST.get("question3", None)
    answer_4 = request.POST.get("question4", None)
    answer_5 = request.POST.get("question5", None)
    answer_6 = request.POST.get("question6", None)
    answer_7 = request.POST.get("question7", None)

    answers = [
        answer_1,
        answer_2,
        answer_3,
        answer_4,
        answer_5,
        answer_6,
        answer_7,
    ]

    if answers == correct_answers:

        return render(request, "base.html")
    else:
        return render(request, "partials/footer.html")

    return render(request, "base.html")

#2. 퀴즈 목록 화면---------------------------------------------------
class QuizList(ListView):
    model = Quiz
    template_name = 'list.html'

#5. 퀴즈 랭킹 화면---------------------------------------------------
class RankingList(ListView):
    model = Ranking
    rank = Ranking.objects.all().order_by('-number')
    template_name = 'ranking.html'


#2. 퀴즈 목록 화면---------------------------------------------------
class QuizList(ListView):
    model = Quiz
    template_name = 'list.html'

#5. 퀴즈 랭킹 화면---------------------------------------------------
class RankingList(ListView):
    model = Ranking
    rank = Ranking.objects.all().order_by('-number')
    template_name = 'ranking.html'


