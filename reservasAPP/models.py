from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_size(value):
    if value > 15:
        raise ValidationError(
            _('El tamaño es mayor a 15 personas')
        )
    elif value < 1:
        raise ValidationError(
            _('El tamaño es menor a 1 persona')
        )    


# Create your models here.
class Reserva(models.Model):
    nombre= models.CharField(max_length=50, blank=False) #Nombre de la persona que reserva
    tel= models.CharField(max_length=13, blank=False) #Telefono
    date= models.DateField(blank=False) #Fecha de la reserva
    time= models.TimeField(blank=False) #Hora de la reserva
    size= models.IntegerField(validators=[validate_size], blank=False)#Cantidad de personas
    status= models.CharField(max_length=50, blank=False)#Estado de la reservación
    desc= models.CharField(max_length=100, blank=True)#Observación de la reserva
     
     
     
    