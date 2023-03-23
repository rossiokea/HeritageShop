# Install python
FROM python:3.10-slim-buster
# RUN python -m pip install --upgrade pip

# Install sqlite3 into container
#FROM ubuntu:trusty
#RUN sudo apt-get -y update
#RUN sudo apt-get -y upgrade
#RUN sudo apt-get install -y sqlite3 libsqlite3-dev


WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# Install sqlite3 into container
#FROM ubuntu:trusty
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev


COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000