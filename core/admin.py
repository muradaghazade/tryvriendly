from django.contrib import admin
from core.models import BetaUsers
from django.contrib.auth.models import Group

admin.site.site_header = "Vriendly"
admin.site.index_title = "Vriendly"
admin.site.site_title = "Vriendly Administration"

admin.site.register([BetaUsers, ])
admin.site.unregister(Group)