from django.contrib import admin

# Register your models here.
from .models import donars,recipient,Frontier_user
admin.site.register(donars)
admin.site.register(recipient)
admin.site.register(Frontier_user)