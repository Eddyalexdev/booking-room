from django.db import models

class Room(models.Model):

# Create your models here.
class Booking(models.Model):
    #all states
    type_state = ["Pendiente", "Pagado", "Eliminado"]

    #model to booking
    days = models.IntegerField(default=0)
    state = models.CharField(max_length=50, choices=type_state, default="Pendiente")
    amount = models.FloatField(default=0)
    method = models.CharField(max_length=100)

