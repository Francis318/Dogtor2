"""API SERIALIZERS"""
from . import models
from rest_framework import serializers

class OwnerModelSerializer(serializers.ModelSerializer):
    """Owner model serializer"""
    class Meta:
        model=models.Owner
        fields=("id", "first_name", "last_name", "email", "phone", "mobile")

class SpeciesModelSerializer(serializers.ModelSerializer):
    """Owner model serializer"""
    class Meta:
        model=models.Species
        fields=("id", "name")
     
class PetModelSerializer(serializers.ModelSerializer):
    """Owner model serializer"""
    class Meta:
        model=models.Pet
        fields=("id", "name", "owner", "email", "age", "species", "created_at")
        read_only_fields=("created_at")

class RecordModelSerializer(serializers.ModelSerializer):
    """Owner model serializer"""
    class Meta:
        model=models.Record
        fields=("id", "category", "procedure", "pet", "date")
