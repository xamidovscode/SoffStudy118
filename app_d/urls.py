from django.urls import path
from . import views

urlpatterns = [
    path("question10/<int:pk>/", views.question_10),
    path("question11/<int:pk>/", views.question11),
    path("question12/<int:pk>/", views.question12),
    path("question13/<int:pk>/", views.question13),
    path('question17/', views.question17),
    path('question20/', views.question20)
]