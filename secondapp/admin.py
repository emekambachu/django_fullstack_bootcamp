from django.contrib import admin
from . models import User

# create class to add products to admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(User, UserAdmin)
