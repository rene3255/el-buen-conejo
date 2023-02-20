from resources.models import State, City
from resources.utils import reset_autoincrement_sql_tables
from farms.models import ProducerProfile
from users_control.models import CustomUser
import csv
from datetime import datetime
from django.db import connection

def run():
  print("Initializing catalogs...")
  reset_auto_increment()
  print("Database tables deleted...")
  add_states()
  print("States catalog created...")
  add_cities()
  print("Cities catalog created...")
  add_producers_profiles()
  print("Producers added...")

def add_custom_user():
    with open('scripts/states_list.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            print(row)
            state = State(state=row[1],  
                      
                        )
            state.save()
  
def add_states():
    with open('scripts/states_list.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            print(row)
            state = State(state=row[1],  
                      
                        )
            state.save()
    
def add_cities():
    with open('scripts/cities_list.csv') as file:
        reader = csv.reader(file)
        next(reader) # Advance past the header
        
        for row in reader:
            print(row[1],row[2])
            city = City(state = State.objects.get(id=row[1]),
                        city = row[2],
                        created_at = datetime.now())
            
            city.save()

def add_producers_profiles():
    with open('scripts/producers.csv') as file:
        reader = csv.reader(file)
        next(reader) # Advance past the header

        for row in reader:
            print("record: ",row)
            
            producer = ProducerProfile(first_name = row[1],
                        last_name = row[2],
                        photo = row[3],
                        farm_name = row[4],
                        address = row[5],
                        producer = CustomUser.objects.get(id=row[6]),
                        city = City.objects.get(id=row[7])
                     
                        )
            
            producer.save()

def reset_auto_increment():
    with connection.cursor() as cursor:
        cursor.execute(reset_autoincrement_sql_tables())
         
    