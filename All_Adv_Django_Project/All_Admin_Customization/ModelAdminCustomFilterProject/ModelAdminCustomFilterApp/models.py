from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role_choices=(
        ("1","Customer"),
        ("2","Editor"),
        ("3","Author"),
        ("4","Staff"),
        )
    roles=models.CharField(max_length=100,choices=role_choices,default="1")
    is_active=models.BooleanField(default=False,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return self.user.email

    @property
    def full_name(self):
        return self.user.first_name + ' ' +self.user.last_name

    def __str__(self):
        return self.user.username



