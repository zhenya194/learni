install:
	pip install -r requirements.txt

run:
	python web/manage.py makemigrations
	python web/manage.py migrate
	python web/manage.py runserver
