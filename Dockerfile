from python:slim

workdir /opt

copy . .

run pip3 install -r requirements.txt && \
 python3 -m unittest echo_test.py

entrypoint gunicorn -b 0.0.0.0:$PORT main:app

