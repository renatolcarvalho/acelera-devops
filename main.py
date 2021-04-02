from flask import Flask
import echo
import ping

app = Flask(__name__)

app.add_url_rule("/ping/<message>", view_func=ping.ping, methods=["GET"])
app.add_url_rule("/echo/<text>", view_func=echo.echo, methods=["GET"])

