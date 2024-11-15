from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
    inlines = [CartTabAdmin, OrderTabulareAdmin]

# admin.site.register(User, UserAdmin)
