from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.conf import settings


User = get_user_model()


class BaseProfile(models.Model):
    """
    Used to extend all profiles
    NOTE: only to be used with profiles model, or will create an error.
    """

    class Meta:
        abstract = True

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)