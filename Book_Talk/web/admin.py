from django.contrib import admin

from Book_Talk.web.forms.user_forms import UserRegisterForm
from Book_Talk.web.models import User, Book


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserRegisterForm


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

