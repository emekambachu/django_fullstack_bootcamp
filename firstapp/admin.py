from django.contrib import admin

from secondapp.models import User

#import access records and topic from models
from . models import AccessRecord, Topic, Webpage

#must create super user before you can access tables in python admin

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

