from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.get_products),
    path("products2/", views.get_products2),
    path("products-post/", views.post_product),
    path("create-user/", views.create_user),
    path("question4/", views.question_four),
    path("question5/", views.question_5),
    path("question9/<int:pk>/", views.question_9),

]


