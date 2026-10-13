from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()

class IDcard(models.Model):
    idcardnumber = models.CharField()
    issuedata = models.DateField()
    student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='jd')