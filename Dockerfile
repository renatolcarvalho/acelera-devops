from python:slim as env

copy requirements.txt .

run pip3 install -r requirements.txt


from env as app

copy *[^test].py .


from app as tester

copy *_test.py .

run python3 -m unittest discover -p *_test.py


from app

entrypoint gunicorn -b 0.0.0.0:$PORT main:app

