from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Workers)
admin.site.register(models.Urls)
admin.site.register(models.Profile_users)
admin.site.register(models.BotAdmins)
admin.site.register(models.Card)