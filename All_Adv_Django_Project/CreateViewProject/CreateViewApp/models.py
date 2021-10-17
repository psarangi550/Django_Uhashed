from django.db import models
from django.urls import reverse
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("thanks")
