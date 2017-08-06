FROM python:latest
RUN mkdir -p /opt/app
COPY . /opt/app
WORKDIR /opt/app
RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip-compile -o requirements/prod.txt requirements/prod.in
run pip-sync requirements/prod.txt
EXPOSE 8000
CMD ["python", "src/runserver.py"]
