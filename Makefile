all:
	ls

say:
	echo "HELLO"

go-venv:
	source venv/bin/activate

quit-venv:
	deactivate
