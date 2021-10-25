from django.db import models

# Create your models here.
class Image(models.Model):
    photos=models.ImageField(upload_to=True)
    update_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photos.name
