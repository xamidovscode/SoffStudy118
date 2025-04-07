from django.urls import path
from . import views

urlpatterns=[
    path("question_7/", views.question_7),
    path("question_8/", views.question_8),
    # path("question_10/<int:pk>/", views.question_10),
    path("question_11/<int:pk>/", views.question_11),
    path("question_13/<int:pk>/", views.question_13),
    path("question_14/<int:pk>/", views.question_14),
]