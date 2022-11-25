from .user import User
from ..models.base_profile import BaseProfile
from django.db import models
from django.conf import settings


class Client(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        User.objects.filter(id=self.user.id).update(is_client=True)
        super().save(*args, **kwargs)