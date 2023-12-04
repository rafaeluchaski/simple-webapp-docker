FROM python:3.9-alpine3.17

RUN pip install flask

COPY app.py /opt/

USER 1001

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
