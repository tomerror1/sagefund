from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from app.models import Deposit, Asset, Deposit_Securities, Transaction, Portfolio, Portfolio_securities

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Deposit)
admin.site.register(Asset)
admin.site.register(Deposit_Securities)
admin.site.register(Transaction)
admin.site.register(Portfolio)
admin.site.register(Portfolio_securities)