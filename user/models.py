from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField('Nombre', max_length=50)
    CI = models.CharField('Carnet de Identidad', max_length=50, unique=True)

    def __str__(self):
        return self.name + ' ' + self.CI
