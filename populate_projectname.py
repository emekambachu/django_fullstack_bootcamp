#import Operating System
import os

#set location for project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')

#import django setup
import django
django.setup()

# fake population script
#import random
import random

#import models from application we want to populate
from firstapp.models import AccessRecord, Webpage, Topic

#import Faker from faker (Note that they are case sensitive)
from faker import Faker

#create an instance for Faker() class
fakegen = Faker()

# add values in topic list
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

#create a function to add items in topic list
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


# create function to populate the tables
def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new #webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record for that web page
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete")