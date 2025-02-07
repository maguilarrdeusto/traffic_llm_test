from rest_framework import serializers
from .models import OptimizationRequest

class OptimizationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimizationRequest
        fields = '__all__'  # Incluir todos los campos