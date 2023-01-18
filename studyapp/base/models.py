from django.db import models
from django.contrib.auth.models import AbstractUser


# Defining custom user not the default one
class User(AbstractUser):
    pass


# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Room(models.Model):
#     host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # Does not delete topic
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)  
#     participants = models.ManyToManyField(User, related_name='participants', blank=True) # We can't have the user because we already have it at the top
#     created = models.DateTimeField(auto_now_add=True) # Updates value only once
#     updated = models.DateTimeField(auto_now=True) # Updated every time it is saved

#     class Meta:
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return self.name


# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE) # One to many relationship
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True) # Updates value only once
#     updated = models.DateTimeField(auto_now=True) # Updated every time it is saved

#     class Meta:
#         ordering = ['-updated', '-created']

#     def __str__(self):
#         return self.body[0:50] # First 50 characters
