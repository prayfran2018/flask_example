import socket
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render_page():
    return render_template("index.html")

@app.route('/animals/')
def animals():
    return render_template("animals.html")

@app.route("/hostname/")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)

