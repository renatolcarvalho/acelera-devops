from python:slim 

copy . /opt

run pip3 install -r /opt/requirements.txt

entrypoint gunicorn -b 0.0.0.0:$PORT --pythonpath /opt main:app

