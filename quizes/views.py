from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

def home(request):
    return HttpResponse("making views")

def list(request):  ################
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = ' || '.join([q.question_text for q in latest_question_list])
   # context = {'latest_question_list': latest_question_list}
    return HttpResponse(context)
   # return render(request, 'quizes/list.html', context)



def create(request):
    return HttpResponse("create")

def quiz(request, question_id):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'quizes/quiz.html', context)


## 위아래 question_id 대응
def detail(request, question_id):
    return HttpResponse("detail")