import json

from django.core import serializers
from django.test import TestCase

from buck.models import Buck
from cage.models import Cage
from doe.models import Doe
from farms.models import ProducerProfile
from mating.models import Mating
from rabbit.models import Rabbit
from resources.models import Breed, City, RabbitStatus, State
from users_control.models import CustomUser
from datetime import date, timedelta

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
        self.rabbit_buck = Rabbit.objects.create(sex="M",breed=self.breed, rabbit_status=self.rabbit_status, cage=self.cage, farm=self.farm)
        self.buck = Buck.objects.create(buck_name="Apolo", buck_rabbit=self.rabbit_buck, farm=self.farm)
        
        # Now instance of Doe 
        self.cage_nodriza = Cage.objects.create(cage_title="Nodriza", farm=self.farm)
        self.breed_nuevazelanda = Breed.objects.create(breed="Nueva Zelanda")
        self.rabbit_status_doe = RabbitStatus.objects.create(status="Doe")
        self.rabbit_doe = Rabbit.objects.create(sex="H",breed=self.breed_nuevazelanda, rabbit_status=self.rabbit_status_doe, cage=self.cage, farm=self.farm)
        self.doe = Doe.objects.create(doe_name="Clara Chia", doe_rabbit =self.rabbit_doe, farm=self.farm)
        
         
       
        
    def tearDown(self) -> None:
        print("Disconnect from database Mating")
    
    def test_mating_database_exists(self):
        self.mating = Mating.objects.create(buck=self.buck, doe=self.doe, observations="Demo", mating_succeeded=True, farm=self.farm)
        self.assertEqual(self.city.state.state, "Venus")
        self.assertEqual(self.city.city, "Berniaka")
        self.assertEqual(self.producer.username, "Juananona")
        self.assertEqual(self.buck.buck_name,"Apolo")
        self.assertEqual(self.doe.doe_name,"Clara Chia")
        self.assertTrue(self.mating)
        #myresult = []
        #myresult = list(Mating.objects.all())
        my_query_set = Mating.objects.all()
        my_json = serializers.serialize('json',my_query_set)
        my_data = json.loads(my_json)
        for item in my_data:
            if item['fields']:
              print(item['fields']) 
              break
    
    def test_mating_date_versus_new_matings(self):
        passes = True
        mating_date_field  = date.today()
        print("Mating Date Test",mating_date_field)
        weaning_field_date = mating_date_field + timedelta(days=50)
        print("Mating Date Test",weaning_field_date)
        self.assertLess(mating_date_field, weaning_field_date)
        print("TEST SUCCEEDED...")
        

    