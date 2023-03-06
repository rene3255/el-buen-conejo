from django.test import TestCase
from django.contrib.auth import get_user_model
from resources.models import State
from scripts import *
import csv
# Create your tests here.
class StateTestCase(TestCase):
  
    def setUp(self):
        print("Setting up test case")

    def tearDown(self): 
        print("Ending test case")
        
    def test_total_records(self):
        with open('scripts/states_list.csv') as file:
            reader = csv.reader(file)
            next(reader)  # Advance past the header
            for row in reader:
                State.objects.create(state=row[1])
      
        print("Checking total records loaded")
        record_set = len(State.objects.all())
        self.assertEqual(32,record_set)
        print("States catalog is complete, total records was successful %s", record_set)
        
    def test_only_one_record(self):
        State.objects.create(state="Colima")
        records = State.objects.filter(state='Colima')
        self.assertEqual('Colima',records[0].state) 
       
      