from flask import Flask, render_template, request, redirect
from flask_sock import Sock

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wdqfegsrdfgj,mnhgsefaw'
sock = Sock(app)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)