from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from carts.admin import ProductCartInline
from users.models import User

# Register your models here.
# admin.site.register(User, UserAdmin)

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
    inlines = [ProductCartInline]