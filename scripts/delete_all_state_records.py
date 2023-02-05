from resources.models import State
def run():
    State.objects.all().delete()
  