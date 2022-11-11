from django.db import models
from django.conf import settings
from profiles.models.coach import Coach
from django.db.models import DecimalField
from trainingProgram.models.category import Category


class Program(models.Model):
    name = models.CharField(max_length=100)
    price = DecimalField(
        max_digits=9,
        decimal_places=2
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)


    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    