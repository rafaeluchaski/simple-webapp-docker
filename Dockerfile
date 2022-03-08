#FROM ubuntu:18.04
FROM registry.redhat.io/ubi8/python-36

RUN pip3 install flask
#RUN apt-get update && apt-get install -y python python-pip
#RUN pip install flask 

COPY app.py /opt/

USER 1001

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
