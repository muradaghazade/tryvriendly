from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from .common import slugify


class User(AbstractUser):
    terms_agreement = models.BooleanField(default=False)
    email = models.EmailField(('email adress'), unique=True, null=True)
    # user_types = models.CharField(max_length=1000000)
    user_type = models.ManyToManyField('UserType',  verbose_name=("User Type"))
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.slug = f'{slugify(self.username)}'
        super(User, self).save(*args, **kwargs)

class UserType(models.Model):
    title = models.CharField(max_length=80)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'

    def __str__(self):
        return f'{self.title}'