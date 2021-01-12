from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    terms_agreement = models.BooleanField(default=False)
    email = models.EmailField(('email adress'), unique=True, null=True)
    user_type = models.ManyToManyField('UserType',  verbose_name=("User Type"))

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class UserType(models.Model):
    title = models.CharField(max_length=80)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'

    def __str__(self):
        return f'{self.title}'