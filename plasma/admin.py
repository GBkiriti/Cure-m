from django.contrib import admin

# Register your models here.
from .models import donars,recipient
admin.site.register(donars)
admin.site.register(recipient)