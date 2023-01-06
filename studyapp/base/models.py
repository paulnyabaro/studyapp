from django.db import models

class Room(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  
    # participants = 
    created = models.DateTimeField(auto_now_add=True) # Updates value only once
    updated = models.DateTimeField(auto_now=True) # Updated every time it is saved

    def __str__(self):
        return self.name
