run-dev:
	$ python -m venv venv
	$ venv/bin/python -m pip install --upgrade pip
	$ venv/bin/python -m pip install pip-tools
	$ venv/bin/pip-compile requirements/dev.in -o requirements/dev.txt
	$ venv/bin/pip-sync requirements/dev.txt
	$ venv/bin/python src/runserver.py

run-prod:
	$ echo "***docker-compose is required***"
	$ docker-compose up

run-tests:
	$ venv/bin/python -m unittest discover -s src

run-prod:
	$ cd src && gunicorn app:app --bind 0.0.0.0:3031 --worker-class sanic.worker.GunicornWorker
