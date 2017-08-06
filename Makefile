run-dev:
	$ python -m venv venv
	$ venv/bin/python -m pip install --upgrade pip
	$ venv/bin/python -m pip install pip-tools
	$ venv/bin/pip-compile requirements/dev.in -o requirements/dev.txt
	$ venv/bin/pip-sync requirements/dev.txt
	$ venv/bin/python src/runserver.py