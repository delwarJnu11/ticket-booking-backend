from django.contrib import admin
from account.models import UserAccount
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(UserAccount,UserAdmin)