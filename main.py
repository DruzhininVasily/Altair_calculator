from flask import Flask, render_template, send_file, request, redirect, url_for, flash, session
from flask_sock import Sock
import json
import data_handling
import db_handler
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
sock = Sock(app)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == "GET":
        return render_template('admin_autorization.html')
    elif request.method == "POST":
        if request.form.get('pass') == os.getenv('ADMIN_PASS'):
            session['user_name'] = 'admin'
            return redirect(url_for('tables'))
        else:
            flash("Пароль не верный!")
            return render_template('admin_autorization.html')


@app.route('/admin/tables', methods=['GET', 'POST'])
def tables():
    try:
        if session['user_name'] == 'admin':
            if request.method == "GET":
                with db_handler.connect_db() as connection:
                    cursor = connection.cursor()
                    sql = "SHOW TABLES;"
                    cursor.execute(sql,)
                    tables_list = cursor.fetchall()
                return render_template('admin_tables.html', tables_list=tables_list)
    except Exception:
        return redirect(url_for('admin'))


@app.route('/admin/table_data', methods=['GET', 'POST'])
def table_data():
    table_name = request.args.get('table_name')
    if request.method == "GET":
        with db_handler.connect_db() as connection:
            cursor = connection.cursor()
            sql = f"SELECT * FROM {table_name};"
            cursor.execute(sql,)
            table_list = cursor.fetchall()
        return render_template('table_detail.html', table_list=table_list, table_name=table_name)
    elif request.method == "POST":
        table_list = []
        for j in range(0, len(request.form.getlist('1'))):
            row = []
            for i in range(1, 8):
                row.append(request.form.getlist(str(i))[j])
            table_list.append(row)
        try:
            with db_handler.connect_db() as connection:
                cursor = connection.cursor()
                for row in table_list:
                    sql = f'''UPDATE `{table_name}`
                        SET `name`=%s, `manufacturer`=%s, `article`=%s, `parameter`=%s, `price`=%s, `groups`=%s
                        WHERE `id` = %s;'''
                    cursor.execute(sql, [row[1], row[2], row[3], row[4], float(row[5]), row[6], int(row[0])])
                connection.commit()
            flash("Записи обновлены")
        except Exception as e:
            print(str(e))
            flash("Ошибка ввода")
        return render_template('table_detail.html', table_list=table_list, table_name=table_name)


@app.route('/specification.xlsx')
def download_file():
    query = request.args.get('name')
    return send_file('specification.xlsx', download_name=f"Спецификация_{query}_{str(datetime.date.today())}.xlsx")


@app.route('/TCP.xlsx')
def download_second_file():
    query = request.args.get('name')
    return send_file('TCP.xlsx', download_name=f"ТКП_{query}_{str(datetime.date.today())}.xlsx")


@app.route('/schema.pdf')
def download_schema():
    query = request.args.get('name')
    return send_file('schema.pdf', download_name=f"Схема_{query}_{str(datetime.date.today())}.pdf")


@sock.route('/')
def receiver(sock):
    handler = data_handling.MessageHandler()
    while True:
        receive_message = {}
        new_message = sock.receive()
        new_message = json.loads(new_message)
        if "type" in new_message:
            receive_message['type'] = new_message['type']
            receive_message['img_list'] = handler.add_type(new_message['type'])
            price, signals = handler.calculate()
            receive_message['price'] = price
            receive_message['signals'] = signals
        elif 'get_exel' in new_message:
            receive_message = handler.create_docs()
        else:
            handler.add_parameters(new_message)
            price, signals = handler.calculate()
            receive_message['price'] = price
            receive_message['signals'] = signals
            receive_message['img_list'] = handler.img_list
        receive_message = json.dumps(receive_message)
        sock.send(receive_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')