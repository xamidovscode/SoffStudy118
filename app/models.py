from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def __str__(self):
            return self.name


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    customer_name = models.CharField(max_length=255)
    product = models.ForeignKey(
        Product, related_name="orders", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"



class OldOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    order = models.ForeignKey(
        Order, related_name="old_orders", on_delete=models.CASCADE, null=True
    )
    customer_name = models.CharField(max_length=255)
    product = models.ForeignKey(
        Product, related_name="old_orders", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()




