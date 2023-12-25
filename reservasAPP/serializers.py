from rest_framework import serializers
from reservasAPP.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    
    #validación campo vacío
    def validate_empty(self, value):
        if value == '':
            raise serializers.ValidationError('Este campo no puede ser vacío')
        return value
    
    #validación cantidad de gente
    def validate_size(self, value):
        if 1>value or value>15:
            raise serializers.ValidationError('La cantidad no puede ser menor a 1 o mayor a 15 personas')
        return value
    
    class Meta:
        model= Reserva
        fields= '__all__'