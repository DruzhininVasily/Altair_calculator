from flask import Flask, render_template, send_file, request, redirect
from flask_sock import Sock
import json
import data_handling

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wdqfegsrdfgj,mnhgsefaw'
sock = Sock(app)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/specification.xlsx')
def download_file():
    return send_file('specification.xlsx')


@sock.route('/')
def receiver(sock):
    handler = data_handling.MessageHandler()
    while True:
        receive_message = {}
        new_message = sock.receive()
        new_message = json.loads(new_message)
        print(new_message)
        if "type" in new_message:
            receive_message['type'] = new_message['type']
            receive_message['img_list'] = handler.add_type(new_message['type'])
            receive_message['price'] = handler.calculate()
        elif 'get_exel' in new_message:
            receive_message = handler.create_exel()
        else:
            handler.add_parameters(new_message)
            receive_message['price'] = handler.calculate()
            receive_message['img_list'] = handler.img_list
        print(receive_message)
        receive_message = json.dumps(receive_message)
        sock.send(receive_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')