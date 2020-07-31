from django.shortcuts import render
from django.contrib.auth.models import User
from quizes.models import Quiz


# Render Quiz Solving Page
def make_quiz(request):
    user = request.user

    context = {
        "user": user,
    }

    if request.method == "GET":
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


def solve_quiz(request):
    # return render(request, "")
    pass
