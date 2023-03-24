from django.test import TestCase
from mating.models import Mating
from buck.models import Buck
from doe.models import Doe
from rabbit.models import Rabbit
from cage.models import Cage
from farms.models import ProducerProfile
from users_control.models import CustomUser
from resources.models import State, City, Breed, RabbitStatus
import json
from django.core import serializers
# Create your tests here.

class MatingTestCase(TestCase):
      
      
    def setUp(self):
        self.state = State.objects.create(state="Venus")
        self.city = City.objects.create(city="Berniaka", state=self.state)
        self.producer = CustomUser.objects.create(username="Juananona")
        self.farm = ProducerProfile.objects.get(id=self.producer.id)
        self.cage = Cage.objects.create(cage_title="Memories", farm=self.farm)
        self.breed = Breed.objects.create(breed="Mariposa")
        self.rabbit_status = RabbitStatus.objects.create(status="Buck")
        self.rabbit_buck = Rabbit.objects.create(rabbit_tag="ebc-030",sex="M",breed=self.breed, rabbit_status=self.rabbit_status, cage=self.cage)
        self.buck = Buck.objects.create(buck_name="Apolo", buck_rabbit=self.rabbit_buck)
        
        # Now instance of Doe 
        self.cage_nodriza = Cage.objects.create(cage_title="Nodriza", farm=self.farm)
        self.breed_nuevazelanda = Breed.objects.create(breed="Nueva Zelanda")
        self.rabbit_status_doe = RabbitStatus.objects.create(status="Doe")
        self.rabbit_doe = Rabbit.objects.create(rabbit_tag="ebc-031",sex="H",breed=self.breed_nuevazelanda, rabbit_status=self.rabbit_status_doe, cage=self.cage_nodriza)
        self.doe = Doe.objects.create(doe_name="Clara Chia", doe_rabbit =self.rabbit_doe)
        
         
       
        
    def tearDown(self) -> None:
        print("Disconnect from database Mating")
    
    def test_mating_database_exists(self):
        self.mating = Mating.objects.create(buck=self.buck, doe=self.doe, vote=2)
        self.assertEqual(self.city.state.state, "Venus")
        self.assertEqual(self.city.city, "Berniaka")
        self.assertEqual(self.producer.username, "Juananona")
        self.assertEqual(self.buck.buck_name,"Apolo")
        self.assertEqual(self.doe.doe_name,"Clara Chia")
        self.assertTrue(self.mating)
        myresult = []
        myresult = list(Mating.objects.all())
        my_query_set = Mating.objects.all()
        my_json = serializers.serialize('json',my_query_set)
        my_data = json.loads(my_json)
        for item in my_data:
            if item['fields']:
              print(item['fields']) 
              break