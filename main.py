from flask import Flask

app = Flask(__name__)

@app.route("/ping/<message>")
def echo(message):
    return f'pong:{message}' 

