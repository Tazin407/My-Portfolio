from django.contrib import admin
from .import models

admin.site.register(models.Skill)
admin.site.register(models.Contact)
admin.site.register(models.Project)

# Register your models here.
