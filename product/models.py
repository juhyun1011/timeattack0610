from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "my_category"

    name = models.CharField(max_length=20, null=False)


class Product(models.Model):
    class Meta:
        db_table = "my_product"

    name = models.CharField(max_length=256, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=1000, null=False)
    price = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)

class OrderStatus(models.Model):
    class Meta:
        db_table = "my_orderstatus"

    status = models.CharField(max_length=256, null=False)