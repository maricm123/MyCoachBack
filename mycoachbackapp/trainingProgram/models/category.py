from django.db import models
from django.conf import settings


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    