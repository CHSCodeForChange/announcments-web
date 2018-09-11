from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Announcement(models.Model):

    #when referencing announcement as a string,
    #it will return its title 
    def __str__(self):
        return 'Announcement: ' + self.title
    objects = models.Manager()

    #title of the announcement
    title = models.CharField(max_length=120)

    #actual announcement to be read
    description = models.CharField(blank=True, max_length=960)
