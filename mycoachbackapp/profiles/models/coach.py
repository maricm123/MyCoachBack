from .user import User
from ..models.base_profile import BaseProfile
from django.db import models
from django.conf import settings


class Coach(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    biography = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username