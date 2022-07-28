from django.db import models
from postings.models import Posting

class Question(models.Model):
    qTypes=[('T','text'),('TA','textarea'),('C','choice')]
    question=models.CharField(max_length=10000)
    type=models.CharField(max_length=10,choices=qTypes)
    post=models.ForeignKey(Posting,on_delete=models.CASCADE)
    choices=models.TextField(null=True,blank=True)

