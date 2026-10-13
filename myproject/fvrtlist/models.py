from django.db import models

# Create your models here.
class fvrtmodel(models.Model):
    name = models.CharField()
    fvrtactor = models.CharField()
    fvrtactress = models.CharField()
    movie = models.CharField()
    media = models.ImageField(upload_to='uploads/')
    
