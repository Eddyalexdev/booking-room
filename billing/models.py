from django.db import models
from datetime import datetime

# Create your models here.

class Billing(models.Model):
    #proveedor
    proveedor_name = models.CharField(max_length=50)
    proveedor_location = models.CharField(max_length=50)
    proveedor_phone = models.CharField(max_length=50)

    #data
    number = models.CharField(max_length=50)
    date_init = models.DateTimeField(default = datetime.now)

