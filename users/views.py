from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    # user = User.objects.get()
    return render(request, "users/home.html")
