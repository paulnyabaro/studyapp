from django.db import models

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True)  
