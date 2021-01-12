from django.contrib import admin
from accounts.models import User, UserType

admin.site.register([User, UserType])
