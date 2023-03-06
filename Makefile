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
