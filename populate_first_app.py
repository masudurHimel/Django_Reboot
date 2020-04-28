import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')


import django
django.setup()

# Main stuff starts from here

import random
from faker import Faker
from first_app.models import Topic, Webpage, AccessDate


fakegen = Faker()
TOP_SAMPLE = ['News', 'Game', 'Entertainment']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(TOP_SAMPLE))[0]
    t.save()
    return t

def populate(N=5):
    
    for i in range(N):
        top = add_topic()

        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()


        webpage = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]
        ad = AccessDate.objects.get_or_create(name= webpage, date = fake_date)[0]


if __name__ == '__main__':
    print("Executing")
    populate(5)
    print("Completed")