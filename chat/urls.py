
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view()),
    path('sender', views.sender.as_view()),
]
