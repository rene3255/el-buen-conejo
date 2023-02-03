run:
		python3 manage.py collectstatic --noinput --clear
		python3 manage.py runserver
		
mig:
		python3 manage.py makemigrations

migbis:
		python3 manage.py migrate
require:
		python3 -m pip install -r requirements.txt		

limpia:
		clear
		git branch

test:
		python3 manage.py test