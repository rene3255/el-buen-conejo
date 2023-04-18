from rest_framework import serializers

class BreedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    breed = serializers.CharField()
    
