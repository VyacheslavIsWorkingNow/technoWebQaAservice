
say:
	echo "HELLO"

go-venv:
	source venv/bin/activate

run:
	python manage.py runserver

quit-venv:
	deactivate
