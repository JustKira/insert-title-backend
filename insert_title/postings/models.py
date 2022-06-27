from django.db import models

# Create your models here.
class Posting1(models.Model):
    name = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    name3 = models.CharField(max_length=300)