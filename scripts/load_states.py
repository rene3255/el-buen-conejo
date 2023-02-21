from resources.models import State, City, Breed, RabbitStatus
from resources.utils import reset_autoincrement_sql_tables, \
                            reset_autoincrement_sql_customusers, \
                            reset_autoincrement_sql_rabbit_status, \
                            reset_autoincrement_sql_rabbit_breeds
                            
from farms.models import ProducerProfile
from users_control.models import CustomUser
import csv
from datetime import datetime
from django.db import connection

def run():
  print("Initializing catalogs...")
  reset_auto_increment_custom_users()
  
  print("Database tables deleted...")
  add_custom_user()
  print("User created...")
  reset_auto_increment()
  add_states()
  print("States catalog created...")
  add_cities()
  print("Cities catalog created...")
  reset_auto_increment_breeds()
  add_breeds()
  print("Rabbit breeds added...")
  reset_auto_increment_rabbit_status()
  add_rabbit_status()
  print("Rabbit status added...")
  add_producers_profiles()
  print("Producers added...")

def add_custom_user():
    with open('scripts/customusers.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        for row in reader:
            print(row)
            customusers = CustomUser(password=row[1],  
                          last_login=row[2],
                          is_superuser=row[3],
                          username=row[4],
                          email=row[5],
                          is_staff=row[6],
                          is_active=row[7],
                          is_verified=row[8],
                          date_joined=row[9],
                        )
            customusers.save()
  
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
                        city = City.objects.get(id=row[7]),
                        is_producer = True,
                     
                        )
            
            producer.save()

def add_breeds():
    with open('scripts/breeds.csv') as file:
        reader = csv.reader(file)
        next(reader) # Advance past the header

        for row in reader:
            print("record: ",row)
            
            breed = Breed(breed = row[1],
                        created_at = datetime.now(),
                        
                     )            
            breed.save()


def add_rabbit_status():
    with open('scripts/rabbit_status.csv') as file:
        reader = csv.reader(file)
        next(reader) # Advance past the header

        for row in reader:
            print("record: ",row)
            
            status = RabbitStatus(status = row[1],
                        created_at = datetime.now(),
                        
                     )            
            status.save()


def reset_auto_increment():
    with connection.cursor() as cursor:
        cursor.execute(reset_autoincrement_sql_tables())

def reset_auto_increment_custom_users():
    with connection.cursor() as cursor:
        cursor.execute(reset_autoincrement_sql_customusers())
def reset_auto_increment_rabbit_status():
    with connection.cursor() as cursor:
        cursor.execute(reset_autoincrement_sql_rabbit_status())
def reset_auto_increment_breeds():
    with connection.cursor() as cursor:
        cursor.execute(reset_autoincrement_sql_rabbit_breeds())