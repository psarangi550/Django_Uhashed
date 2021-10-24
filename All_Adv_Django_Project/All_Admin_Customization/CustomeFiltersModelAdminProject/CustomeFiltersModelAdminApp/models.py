from django.db import models

# Create your models here.
class Blog(models.Model):
    role_choices=(
        ("1","Editor"),
        ("2","Author"),
        ("3","Admin")
        )
    title = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    roles=models.CharField(max_length=200,choices=role_choices,blank=True)
