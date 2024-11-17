from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.Serializer):
        nome = serializers.CharField(max_length=100)
        email = serializers.EmailField()

