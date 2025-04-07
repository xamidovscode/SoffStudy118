from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import *

@api_view(['POST'])
def question_10(request, **kwargs):
    pk = kwargs.get('pk')

    order = Order.objects.filter(id=pk).first()

    if not order:
        return Response(
            data={"pk": "Order not Fount"},
            status=404
        )

    new_quantity = request.data.get('quantity', order.quantity)

    order.quantity = new_quantity
    order.price = new_quantity * order.price
    order.save()

    return Response("success")
