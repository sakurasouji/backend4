from django.contrib import admin
from .models import Reserva

# Register your models here.
class reservaAdmin(admin.ModelAdmin):
    list_display = ['nombre','tel','date','time','size','status','desc']
    
admin.site.register(Reserva, reservaAdmin)