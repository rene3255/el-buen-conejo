run:
	    python manage.py runserver

runclear:
		python manage.py collectstatic --noinput --clear
		python manage.py runserver
		
mig:
		python manage.py makemigrations

migbis:
		python manage.py migrate
require:
		python -m pip install -r requirements.txt		

limpia:
		clear
		git branch

test:
		python manage.py test
load:
		python3 manage.py runscript load_states

delete_mig:
		rm -rf ./doe/migrations/00*.py
		rm -rf ./buck/migrations/00*.py
		rm -rf ./users_control/migrations/00*.py
		rm -rf ./resources/migrations/00*.py
		rm -rf ./diary/migrations/00*.py
		rm -rf ./rabbit/migrations/00*.py
		rm -rf ./cage/migrations/00*.py
		rm -rf ./farms/migrations/00*.py
		rm -rf ./mating/migrations/00*.py
