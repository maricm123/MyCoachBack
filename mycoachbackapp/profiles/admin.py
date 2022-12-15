from django.contrib import admin
from .models import User
from .models.client import Client
from .models.coach import Coach
from django.contrib.auth import get_user_model
from rest_framework_simplejwt import token_blacklist

# Register your models here.

User = get_user_model()

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Coach)


class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)