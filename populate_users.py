#import Operating System
import os

#set location for project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')

#import django setup
import django
django.setup()

# fake population script

#import models from application we want to populate
from secondapp.models import User

#import Faker from faker (Note that they are case sensitive)
from faker import Faker

#create an instance for Faker() class
fakegen = Faker()

# create function to populate the tables
def populate(N=5):

    for entry in range(N):

        # create the fake data for that entry

        # create a fake name and split it into two
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        #create the new user entry
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating User table")
    populate(20)
    print("Populating Complete")