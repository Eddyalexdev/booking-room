from django.db import models
from room.models import Room
from user.models import User
from billing.models import Billing

# Create your models here.
class Booking(models.Model):
    #all states
    type_state = [("1", "Pendiente"), ("2", "Pagado"), ("3", "Eliminado")]

    #details room
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    #details billing
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE)

    #model to booking
    days = models.IntegerField('Days', default=0)
    state = models.CharField('State', max_length=50, choices=type_state)
    amount = models.DecimalField('Price',default=0, decimal_places=2, max_digits=10)
    method = models.CharField(max_length=100)

