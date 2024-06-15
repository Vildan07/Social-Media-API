from django.contrib import admin
from .models import UserProfile, Friend, Messages

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Friend)
admin.site.register(Messages)
