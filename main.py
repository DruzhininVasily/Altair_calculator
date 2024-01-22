from flask import Flask, render_template, request, redirect
from flask_sock import Sock
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wdqfegsrdfgj,mnhgsefaw'
sock = Sock(app)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@sock.route('/')
def receiver(sock):
    while True:
        new_message = sock.receive()
        new_message = json.loads(new_message)
        print(new_message)
        if "type" in new_message:
            new_message = json.dumps(new_message)
            sock.send(new_message)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)