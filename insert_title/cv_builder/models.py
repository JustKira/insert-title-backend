from django.db import models

# Create your models here.
class CV_Template(models.Model):

    ## Taken from old project
    # Templates will be saved as django template files with code names i.e. "3.html", "45.html". This will be used to link.
    template_code = models.IntegerField(unique=True)

    time_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # In case of standardized forms that are accepted or required for certain institutions:
    # Name of standardized form
    template_name = models.TextField()
    # List form of institutions which support this document
    institutions = models.TextField()