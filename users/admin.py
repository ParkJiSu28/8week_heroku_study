from django.contrib import admin
from .models import CustomerUser

from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomerUserAdmin(UserAdmin):
    model = CustomerUser
    list_display = ['email', 'name']


admin.site.register(CustomerUser, CustomerUserAdmin)
