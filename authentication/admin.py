from django.contrib import admin

# Register your models here.
from .models import User
from .models import *
# Register your models here.
admin.site.register(Profile)


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']


admin.site.register(User, UserAdmin)
