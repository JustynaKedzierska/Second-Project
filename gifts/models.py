from django.contrib.auth.models import User
from django.db import models

# Create your models here.

TYPE = [
    ('FUN', 'fundacja'),
    ('ORG', 'organizacja pozarządowa'),
    ('LOK', 'zbiórka lokalna'),
]


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name =models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=64, choices=TYPE, default='fundacja')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=5)
    pick_up_datetime = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)


