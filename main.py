from flask import Flask
import echo
import ping
import failing

app = Flask(__name__)

app.add_url_rule("/ping/<message>", view_func=ping.ping, methods=["GET"])
app.add_url_rule("/echo/<text>", view_func=echo.echo, methods=["GET"])
app.add_url_rule("/failing", view_func=failing.failing, methods=["GET"])

@app.route("/health")
def health():
  return "HTTP: 200 - SUCCESS"
