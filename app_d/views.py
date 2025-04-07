from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import *

@api_view(['POST'])
def question_10(request, **kwargs):
    pk = kwargs.get('pk')
    new_quantity = request.data.get('new_quantity')

    order = Order.objects.filter(id=pk).first()

    if not order:
        return Response(
            data={"pk": "Order not Fount"},
            status=404
        )

    if not order.price:
        return Response(
            data={"price": "Order not Fount"},
            status=404
        )

    order.price = int(new_quantity) * order.price
    order.quantity = new_quantity
    order.save()

    return Response("success")

@api_view(['POST'])
def question11(request, **kwargs):
    pk = kwargs.get('pk')
    new_status = request.data.get('new_status', None)

    order = Order.objects.filter(id=pk).first()

    if not order:
        return Response(
            data={"pk": "Order not Fount"},
            status=404
        )

    if order.status is None:
        return Response(
            data={"status": "Order not Fount"},
            status=404
        )

    if order.status == "completed":
        return Response('Status there is')

    order.status = new_status
    order.save()

    return Response("success")

@api_view(['POST'])
def question12(request, **kwargs):
    pk = kwargs.get('pk')
    new_name = request.data.get('new_name')

    order = Order.objects.filter(id=pk).first()

    if not order:
        return Response(
            data={"pk": "Buyurtma topilmadi"},
            status=404
        )

    old_order = OldOrder.objects.create(
        customer_name=order.customer_name,
        product=order.product,
        quantity=order.quantity,
        price=order.price,
        status=order.status,
        created_at=order.created_at,
        updated_at=order.updated_at
    )
    order.customer_name = new_name
    order.save()

    return Response({"customer_id": old_order.id})


@api_view(['POST'])
def question13(request, **kwargs):
    pk = kwargs.get('pk')

    order = Order.objects.filter(id=pk).first()

    if not order:
        return Response(
            data={"pk": "Order not Fount"},
            status=400
        )

    if order.status=="completed":
        return Response(
            data={"error": "Completed statusdagi buyurtma o‘chirib bo‘lmaydi"}
        )

    order.delete()
    return Response(
        data={"delete":"O'chirildi"},
        status=200
    )




@api_view(['POST'])
def question17(request):
    new_customer = request.data.get('new_customer')
    product = request.data.get('product')
    quantity = request.data.get('quantity')
    price = request.data.get('price')

    if Order.objects.filter(customer_name=new_customer).exists():
        return Response(
            data={"error": "Order Customer already exists!"},
            status=400
        )

    create_order = Order.objects.create(
        customer_name=new_customer,
        product=product,
        quantity=quantity,
        price=price,
    )
    create_order.save()

    return Response("Success")


@api_view(["GET"])
def question20(request):
    orders_count = Order.objects.values('customer_id').annotate(count=Count('id'))

    result = []
    for customer in orders_count:
        result.append({
            "customer_name": customer.count,
        })
    return Response(result)


