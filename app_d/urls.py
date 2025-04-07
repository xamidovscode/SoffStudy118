from django.urls import path
from . import views

urlpatterns = [
    path("question10/<int:pk>/", views.question_10),
]