from django.contrib import admin

# import user model from secondapp
from secondapp.models import User

#import access records and topic from models
from . models import AccessRecord, Topic, Webpage

# must create super user before you can access tables in python admin

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

# create class to add users table to admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(User, UserAdmin)

