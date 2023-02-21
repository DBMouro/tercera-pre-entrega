from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

class Warehouse(models.Model):
    alias = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity_in_m3 = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    cooling_system = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)