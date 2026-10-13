from django.db import models


# Create your models here.
class bmwlist(models.Model):
    title=models.CharField(max_length=50)
    para = models.CharField()
    price = models.CharField()

