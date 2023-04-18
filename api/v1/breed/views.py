from rest_framework.decorators import api_view
from rest_framework.response import Response
from resources.models import Breed
from api.v1.breed.serializers import BreedSerializer

@api_view(['GET','POST'])
def breed_list(request):
    breed = Breed.objects.all().order_by('-id')
    serializer = BreedSerializer(breed, many=True)
    return Response(serializer.data)
