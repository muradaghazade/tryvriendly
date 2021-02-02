from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from .common import slugify
import uuid

class User(AbstractUser):
    terms_agreement = models.BooleanField(default=False)
    email = models.EmailField(('email adress'), unique=True, null=True)
    # user_types = models.CharField(max_length=1000000)
    user_type = models.ManyToManyField('UserType', verbose_name=("User Type"))
    slug = models.SlugField(max_length=255, null=True, blank=True)
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

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

class CreateIvent(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,
                                 editable=False,
                                 unique=True,
                                 blank=False,
                                 null=False,
                                 max_length=8)


    event_name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Create Room"
        verbose_name_plural = "Create Rooms"

    def __str__(self):
        return f'{self.event_name}'


class GetRooms(models.Model):
    thumbnail_link = models.URLField(max_length=200,null=True,blank=True)
    room_name = models.CharField(max_length=80,blank=True)
    desc = models.TextField(null=True,blank=True)


    def __str__(self):
        return f'{self.room_name}'
