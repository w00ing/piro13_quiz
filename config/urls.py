from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("users.urls")),
    path("quizes/", include("quizes.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
]
