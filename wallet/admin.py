from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import User, Elite, Noob, Wallet, Transactions

# Register your models here

class UsersAdmin(UserAdmin):
    ordering=("email",)

admin.site.register(User, UsersAdmin)
admin.site.register(Elite)
admin.site.register(Noob)
admin.site.register(Wallet)
admin.site.register(Transactions)

