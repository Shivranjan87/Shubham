from django.db import models


# Create your models here.

class teacher(models.Model):
    t_name = models.CharField(max_length=30)
    t_mname = models.CharField(max_length=30)
    t_lname = models.CharField(max_length=30)
    t_age = models.IntegerField()
    t_add = models.CharField(max_length=40)
    t_qual = models.CharField(max_length=10)
    t_gender = models.CharField(max_length=40, choices=[('M', 'Male'), ('F', 'Female')])
