FROM python:latest

WORKDIR /

ADD ./src /src

COPY ./requirements.txt /etc

RUN pip install -r /etc/requirements.txt

RUN apt-get update

RUN apt-get install ffmpeg -y


CMD [ "python", "main.py" ]
