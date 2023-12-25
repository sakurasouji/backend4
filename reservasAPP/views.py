from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from reservasAPP.serializers import ReservaSerializer
from .models import Reserva
from .forms import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

class viewAPI(ListAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['date']
    ordering = ['date']

    #Read y Create en API
    @api_view(['GET', 'POST'])
    def listaReservaAPI(request):
        if request.method == 'GET':
            reservas = Reserva.objects.all()
            #reservas = self.filter_queryset(self.get_queryset())
            serializer = ReservaSerializer(reservas, many= True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            serializer = ReservaSerializer(data = request.data)
            #validación
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Reserva creada correctamente!'})
                #return HttpResponseRedirect(reverse('crAPI'))
            else:
                return Response({'message':'ERROR'})
        
    #Update en API
    @api_view(['POST'])
    def updReservaAPI(request, id):
        if request.method == 'POST':
            reserva = Reserva.objects.get(id=id)
            serializer = ReservaSerializer(instance=reserva, data = request.data)
            #validación
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Reserva guardada correctamente!'})
            else:
                return Response({'message':'ERROR'})
        
    #Delete en API        
    @api_view(['DELETE'])
    def delReservaAPI(request, id):
        if request.method == 'DELETE':
            reserva = Reserva.objects.get(id=id)
            reserva.delete()
            return Response({'message':'Reserva eliminada correctamente!'})

#Read sin API    
def readReserva(request):
    reservas = Reserva.objects.all()
    data = {
        'reservas' : reservas
    }
    return render(request, 'listaReservas.html', data)

#Create sin API    
def createReserva(request):
    if request.method == "POST":
        form = newReservaForm(request.POST, request.FILES)
        if form.is_valid():   
            form.save()
            form.cleaned_data['nombre'] = ''
            form.cleaned_data['tel'] = ''
            form.cleaned_data['date'] = ''
            form.cleaned_data['time'] = ''
            form.cleaned_data['size'] = ''
            form.cleaned_data['status'] = ''
            form.cleaned_data['desc'] = ''
            print("Reserva agregada correctamente")
            return HttpResponseRedirect(reverse('listaReservas'))
            
    else:
        form = newReservaForm()        
    data = {'form': form,
            'titulo_menu': 'Crear Reserva',
            'boton': 'Crear Reserva'
            }
    return render(request, 'createReservas.html', data)

#Update sin API
def editReserva(request, id):
    reserva = Reserva.objects.get(id = id)
    form = newReservaForm(instance=reserva)
    if request.method == "POST":
        form = newReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect(reverse('listaReservas'))                
    data = {'form': form,
            'titulo' : 'Editar Reserva',
            'boton' : 'Aplicar cambios'
            }
    return render(request, 'createReservas.html', data)

#Delete sin API
def delReserva(request, id):
    reserva = Reserva.objects.get(id = id)
    reserva.delete()
    return HttpResponseRedirect(reverse('listaReservas'))            