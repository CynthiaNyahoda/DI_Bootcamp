from rest_framework import serializers
from .models import Animal, Family

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    family = FamilySerializer()

    class Meta:
        model = Animal
        fields = '__all__'
