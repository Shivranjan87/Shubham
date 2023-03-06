from django.db import models


# Create your models here.

class student(models.Model):
    s_name = models.CharField(max_length=30)
    s_mname = models.CharField(max_length=30)
    s_lname = models.CharField(max_length=30)
    s_age = models.IntegerField()
    s_add = models.CharField(max_length=40)
    s_gender = models.CharField(max_length=40, choices=[('M', 'Male'), ('F', 'Female')])
