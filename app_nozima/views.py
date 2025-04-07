from datetime import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from app_nozima.models import Order, OldOrder


@api_view(['GET'])
def question_7(request):
    obj_price = Order.objects.filter(price__gt=500).values_list('status','price')
    return Response({'message': obj_price})




@api_view(['GET'])
def question_8(request):
    status = Order.objects.filter(status='completed').values_list('customer_name','status','price').last()
    return Response({'message': status})




# @api_view(['GET'])
# def question_10(request, **kwargs):
#     pk = kwargs.get("pk")
#     order = Order.objects.filter(id=pk).first()
#     new_quantity= request.data.get("quantity")
#     old_price = order.price
#
#     if order.quantity != new_quantity:
#         order.price = old_price * order.quantity
#
#         order.quantity = new_quantity
#         order.save()
#     return Response(order.values("id", "status", 'quantity','price',"customer_name"))



@api_view(['GET'])
def question_11(request, **kwargs):
    pk = kwargs.get("pk")
    order = Order.objects.filter(id=pk).first()

    if order is not None and order.status == 'completed':
        with open('order_changes.log', 'a') as file:
            file.write(f'{order.id},{order.status}, {order.price}\n, {order.customer_name};')
        return Response({'success'})
    else:
        return Response('not found')





@api_view(['GET'])
def question_13(request, **kwargs):

    pk = kwargs.get("pk")
    order=Order.objects.filter(id=pk).first()

    if order is not None and order.status != 'completed':
        order.delete()
        return Response('not found')
    return Response('success')


@api_view(['DELETE'])
def question_14(request, **kwargs):
    pk = kwargs.get("pk")
    order = Order.objects.filter(id=pk).first()

    if order.delete():
        old_order = OldOrder.objects.create(
            id=order.id,
            status=order.status,
            price=order.price,
            customer_name=order.customer_name,
            product=order.product,
            quantity=order.quantity,
            )
        order.delete()

    return Response('success')



# @api_view(['GET'])
# def question_18(request):