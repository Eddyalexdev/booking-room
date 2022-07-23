from django.db import models
from rooom.models import Room

# Create your models here.
class Booking(models.Model):
    #all states
    type_state = ["Pendiente", "Pagado", "Eliminado"]

    #details room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    #model to booking
    days = models.IntegerField('Days', max_digits=3)
    state = models.CharField('State', max_length=50, choices=type_state, default="Pendiente")
    amount = models.DecimalField('Price',default=0, decimal_places=2, max_digits=10)
    method = models.CharField(max_length=100)

