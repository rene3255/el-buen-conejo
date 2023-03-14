from rest_framework import serializers
from diary.models import Diary

class DiarySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    activity_date = serializers.DateField()
    activity = serializers.CharField(max_length=250)
    costs = serializers.IntegerField()
    farm = serializers.IntegerField()
    
    
    