from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from reservasAPP.models import *


#______________________PRODUCTOS___________________________________#
class newReservaForm(forms.Form):
    ESTADOS = [('reservado', 'RESERVADO'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]
    
    
    nombre= forms.CharField(label= 'Nombre Cliente Reserva', required=True) #Nombre de la persona que reserva
    tel= forms.CharField(label= 'Telefono Cliente Reserva', required=True) #Telefono
    date= forms.DateField(label= 'Fecha de la Reserva', widget= forms.DateInput(attrs={'type': 'date'}), required=True) #Fecha de la reserva
    time= forms.TimeField(label= 'Hora de la Reserva', widget= forms.TimeInput(attrs={'type': 'time'}), required=True) #Hora de la reserva
    size= forms.IntegerField(label= 'Cantidad de personas', required=True)#Cantidad de personas
    status= forms.CharField(label='Estado de la Reserva', widget= forms.Select(choices=ESTADOS), required=True)#Estado de la reservación
    desc= forms.CharField(label= 'Observación', required=False)#Observación de la reserva
    
    nombre.widget.attrs['class'] = 'form-control'
    tel.widget.attrs['class'] = 'form-control'
    date.widget.attrs['class'] = 'form-control'
    time.widget.attrs['class'] = 'form-control'
    size.widget.attrs['class'] = 'form-control'
    status.widget.attrs['class'] = 'form-control'
    desc.widget.attrs['class'] = 'form-control'
    
class newReservaForm(forms.ModelForm):
    ESTADOS = [('reservado', 'RESERVADO'), ('completada', 'COMPLETADA'), ('anulada', 'ANULADA'), ('no asisten', 'NO ASISTEN')]
    
    
    nombre= forms.CharField(label= 'Nombre Cliente Reserva', required=True) #Nombre de la persona que reserva
    tel= forms.CharField(label= 'Telefono Cliente Reserva', required=True) #Telefono
    date= forms.DateField(label= 'Fecha de la Reserva', widget= forms.DateInput(attrs={'type': 'date'}), required=True) #Fecha de la reserva
    time= forms.TimeField(label= 'Hora de la Reserva', widget= forms.TimeInput(attrs={'type': 'time'}), required=True) #Hora de la reserva
    size= forms.IntegerField(label= 'Cantidad de personas', required=True)#Cantidad de personas
    status= forms.CharField(label='Estado de la Reserva', widget= forms.Select(choices=ESTADOS), required=True)#Estado de la reservación
    desc= forms.CharField(label= 'Observación', required=False)#Observación de la reserva
    
    nombre.widget.attrs['class'] = 'form-control'
    tel.widget.attrs['class'] = 'form-control'
    date.widget.attrs['class'] = 'form-control'
    time.widget.attrs['class'] = 'form-control'
    size.widget.attrs['class'] = 'form-control'
    status.widget.attrs['class'] = 'form-control'
    desc.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Reserva
        fields = (
            'nombre',
            'tel',
            'date',
            'time',
            'size',
            'status',
            'desc'
                  
                  )