from django.db import models

# Create your models here.
class message_data(models.Model):
    message_data = models.TextField()
    image = models.ImageField(upload_to='images', blank= True)