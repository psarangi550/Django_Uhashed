import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","updateViewProject.settings")

import django

django.setup()

import random

from faker import Faker

fake=Faker("en-IN")

from updateViewApp.models import Employee

def populate(n):
    for i in range(n):
        eno=random.randint(00,99)
        ename=fake.name()
        esal=random.uniform(0000,9999)
        eaddr=fake.address()
        Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)

populate(20)

