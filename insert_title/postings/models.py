from django.db import models

# Create your models here.

class Posting(models.Model):
    company = models.CharField(max_length=250)
    recruiter = models.CharField(max_length=250)
    image = models.ImageField(upload_to='postings/%Y/%m/%d/', null=True)
    description = models.TextField()

    ##  Based on LinkedIn
    # Auto adds creation date
    creation_date = models.DateTimeField(auto_now_add=True)
    # If 0, unpaid; if more than 0, paid (can be used to diffrentiate in postings frontend)
    pay_range = models.CharField(max_length=250)
    location = models.CharField(max_length=1000)
    # Number of current applicants (can be used to encourage people)
    num_applicants = models.IntegerField(default=0)
