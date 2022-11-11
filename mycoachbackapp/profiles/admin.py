from django.contrib import admin
from .models import User
from .models.client import Client
from .models.coach import Coach
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Coach)