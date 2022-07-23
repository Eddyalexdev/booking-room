from django.db import models

# Create your models here.
class Room(models.Model):
    #all locations for rooms
    location_rooms = ["A1", "A2", "A3", "B1", "B2", "B3"]

    #model Room
    location = models.CharField(max_length=10, choices=location_rooms, unique=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.location + ' ' + self.description
