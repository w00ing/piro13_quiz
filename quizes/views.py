# <<<<<<< HEAD
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

# from users.models import SolvedUser
from quizes.models import Quiz, SolvedUser
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

    # context = {
    #     "title": title,
    #     "answers": [
    #         answer_1,
    #         answer_2,
    #         answer_3,
    #         answer_4,
    #         answer_5,
    #         answer_6,
    #         answer_7,
    #     ],
    # }

    try:
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
        url = reverse("users:home")
        return redirect(to=url)

    except:
        return render(request, "users/existing_user.html")


def solve_quiz(request, pk):
    current_user = request.user
    quiz_owner = User.objects.get(pk=pk)

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
    number_of_matches = 0
    for index, answer in enumerate(answers):
        if answer == correct_answers[index]:
            number_of_matches += 1
    context = {
        "number_of_matches": number_of_matches,
    }

    # solved_user = current_user
    # # solved_user.save()
    # solved_user.quiz.add(current_user.quiz)
    # print(SolvedUser.objects.all())

    return render(request, "quizes/results.html", context=context)


def quiz_list(request):
    current_user = request.user
    quizes = Quiz.objects.order_by("user")

    context = {
        "quizes": quizes,
        "current_user": current_user,
    }

    return render(request, "quizes/quiz_list.html", context=context)


def quiz_ranking(request, pk):
    quiz = request.user.quiz
    solved_users = SolvedUser.objects.filter(solved_quiz=quiz)
    print(solved_users)

    context = {
        "solved_users": solved_users,
    }
    return render(request, "quizes/ranking_list.html", context=context)

