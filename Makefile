gunicorn:
	gunicorn main:application

waitress:
	python run_waitress.py

simple:
	python run_simple.py
