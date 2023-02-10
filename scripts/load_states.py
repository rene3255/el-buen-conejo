from resources.models import State
import csv


def run():
    with open('scripts/states_list.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        State.objects.all().delete()
    
        for row in reader:
            print(row)
            state = State(state=row[1],  
                       
                        )
            state.save()
