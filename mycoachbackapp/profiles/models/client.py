from .user import User
from ..models.base_profile import BaseProfile
from django.db import models
from django.conf import settings

class ClientParameters(models.Model):
    class Meta:
        abstract = True

class Client(ClientParameters, BaseProfile):
    

    def __str__(self):
        return self.client.username