FROM python:3.9.9-alpine3.13

WORKDIR /app

COPY ./requirements.txt  /app

RUN pip install ruamel.yaml.clib && pip install -r requirements.txt

COPY . /app

CMD [ "python3", "coffee_machine.py" ]