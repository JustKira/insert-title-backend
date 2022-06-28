from django.db import models

# Create your models here.
class Career(models.Model):

    ## Taken from old project
    standard_skills = models.TextField()
    recommended_projects = models.TextField()
    soft_skills = models.TextField()
    frameworks = models.TextField()

    # define structure (probably dictonary of milestones) i.e. {"Phase1" : [standard_skills_1, rec_projects_1, ], "Phase2" : [framework_1, soft_skills_1, standard_skills_2]}
    roadmap = models.TextField()