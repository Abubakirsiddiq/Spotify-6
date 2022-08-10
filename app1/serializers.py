from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class AktyorSer(serializers.ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'


class KinoSer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

