from django.db import models

# Create your models here.

class Reserva(models.Model):  
    hotel = models.CharField(max_length=120, verbose_name='Hotel') 
    destino = models.CharField(max_length=100, verbose_name='Destino')
    pasajeros = models.IntegerField(verbose_name='PAX')
    fecha_arribo = models.DateField(verbose_name='Fecha de Arribo')
    
    def __str__(self):
        return f"{self.hotel} {self.destino} {self.pasajeros} - ({self.fecha_arribo})"    

