from rest_framework import serializers

from cars.models import Cars, Moto


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'