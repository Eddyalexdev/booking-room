from django.db import models

# Create your models here.
class Room(models.Model):
    #all locations for rooms
    location_rooms = (("1", "A1"), ("2", "A2"), ("3", "B1"))

    #model Room
    location = models.CharField(max_length=10, choices=location_rooms)
    description = models.CharField(max_length=500)
    avaiable = models.BooleanField(default=True)

    def __str__(self):
        return self.location + ' ' + self.description 
