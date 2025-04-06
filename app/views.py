from datetime import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from app.models import *


@api_view(['GET'])
def get_products(request):
    name = request.query_params.get("name", None)

    if name in (None, ""):
        raise ValidationError(
            {"message": f"Ism kiritilmadi"}
        )

    return Response({"message": f"Message {name}"})


@api_view(['GET'])
def get_products2(request):
    num1 = request.query_params.get("num1", None)
    num2 = request.query_params.get("num2", None)

    if num1 in (None, "") or num2 in (None, ""):
        raise ValidationError(
            {"message": f"num1 yoki num2 kiritilmadi"}
        )

    if not (num1.isdigit() and num2.isdigit()):
        raise ValidationError(
            {"message": f"faqat son kiritish mumkin"}
        )

    return Response({"message": f"Message {int(num1) + int(num2)}"})


@api_view(['POST'])
def post_product(request):
    name = request.data.get("name", None)
    age = request.data.get("age", None)

    if (name or age) is None:
        raise ValidationError({"name_or_age": "Required"})

    return Response({"response": f"Foydalanuvchi {name} {age} yoshda"})


@api_view(['POST'])
def create_user(request):
    username = request.data.get("username", None)
    password = request.data.get("password", None)

    if username is None or password is None:
        raise ValidationError({"msg": "Required"})

    if User.objects.filter(username=username).exists():
        raise ValidationError({"msg": "Bunday foydalanuvchi mavjud"})

    user = User.objects.create(
        username=username,
        password=password
    )

    return Response({"response": f"Foydalanuvchi {user.id} yaratildi"})


# 4 question
@api_view(['GET'])
def question_four(request):
    orders = Order.objects.all().order_by('-created_at')
    return Response(orders.values("id", "status", "created_at"))


# 5 question
@api_view(['GET'])
def question_5(request):
    customer_name = request.query_params.get("name")
    orders = Order.objects.all()

    if customer_name:
        orders = orders.filter(customer_name=customer_name)

    return Response(orders.values("id", "status", "customer_name"))


# 6 question
@api_view(['GET'])
def question_5(request):
    start_date_str = request.query_params.get("start_date")
    end_date_str = request.query_params.get("end_date")

    orders = Order.objects.all()

    if start_date_str and end_date_str:

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError({"date": "Unsupported date format"})
        else:
            orders = orders.filter(
                created_at__date__gte=start_date,
                created_at__date__lte=end_date,
            )

    return Response(
        orders.values("id", "status", "created_at__date"),
        status=200
    )


@api_view(['POST'])
def question_9(request, **kwargs):

    pk = kwargs.get("pk")
    order = Order.objects.filter(id=pk).first()

    if not order:
        return Response(
            data={"pk": "Order not Found"},
            status=404
        )

    new_status = request.data.get("status", order.status)

    if new_status == "canceled" and order.status != "canceled":
        order.updated_at = datetime.now()

    order.status = new_status
    order.save()

    return Response("success")

