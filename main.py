from flask import Flask, render_template, send_file, request, redirect, url_for, flash, session
from flask_sock import Sock
from exchange_rate import get_rate
from create_specification import add_tcp_name, create_general_tcp
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

rate_date = datetime.datetime(1900, 1, 1)
rate = 100.0


@app.route("/", methods=['GET', 'POST'])
def admin():
    if request.method == "GET":
        try:
            user_name = session['user_name']
        except Exception:
            user_name = ''
        if user_name == 'admin' or user_name == 'user':
            return redirect(url_for('main'))
        else:
            return render_template('admin_autorization.html')
    elif request.method == "POST":
        if request.form.get('name') == 'admin' or request.form.get('name') == 'user':
            session['user_name'] = request.form.get('name')
            if request.form.get('pass') == os.getenv('ADMIN_PASS') and session['user_name'] == 'admin':
                return redirect(url_for('main'))
            elif request.form.get('pass') == os.getenv('USER_PASS') and session['user_name'] == 'user':
                return redirect(url_for('main'))
            else:
                flash("Пароль не верный!")
                return render_template('admin_autorization.html')
        else:
            flash("Логин не верный!")
            return render_template('admin_autorization.html')


@app.route("/main", methods=['GET', 'POST'])
def main():
    data = []
    try:
        user_name = session['user_name']
    except Exception:
        user_name = ''
    if user_name == 'admin' or user_name == 'user':
        if request.method == 'GET':
            with db_handler.connect_db() as connection:
                tcps = db_handler.get_all_tcp(connection)
            for tcp in tcps:
                tcp = list(tcp)
                with db_handler.connect_db() as connection:
                    prices = db_handler.get_tcp_price((int(tcp[0]), ), connection)
                    price = 0
                    for p in prices:
                        price += p[0] * p[1]
                    tcp[8] = price
                    data.append(tcp)
        elif request.method == 'POST':
            new_tcp = request.form.to_dict()
            with db_handler.connect_db() as connection:
                date_time = datetime.datetime.now()
                date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
                db_handler.create_tcp(
                    new_tcp['company_name'],
                    new_tcp['company_object'],
                    new_tcp['tcp_number'],
                    new_tcp['customer'],
                    new_tcp['executor'],
                    date_time,
                    '0',
                    0,
                    connection
                )
                tcps = db_handler.get_all_tcp(connection)
            for tcp in tcps:
                tcp = list(tcp)
                with db_handler.connect_db() as connection:
                    prices = db_handler.get_tcp_price((int(tcp[0]),), connection)
                    price = 0
                    for p in prices:
                        price += p[0] * p[1]
                    tcp[8] = price
                    data.append(tcp)
        return render_template('main.html', data=data, user=user_name)
    else:
        return redirect(url_for('admin'))


@app.route("/logout", methods=['GET'])
def logout():
    if session['user_name']:
        session['user_name'] = ''
    return redirect(url_for('admin'))


@app.route("/systems", methods=['GET', 'POST'])
def systems():
    try:
        user_name = session['user_name']
    except Exception:
        user_name = ''
    if user_name == 'admin' or user_name == 'user':
        types = {
            '{"type": "In_out"}': 'Приточно-вытяжная',
            '{"type": "In"}': 'Приточная',
            '{"type": "Out"}': 'Вытяжная'
        }
        if request.method == 'GET':
            data = []
            tcp_id = request.args.get('tcp_id')
            tcp_number = request.args.get('tcp_number')
            with db_handler.connect_db() as connection:
                system = db_handler.get_tcp_configs((tcp_id,), connection)
            for s in system:
                s = list(s)
                try:
                    s[6] = types[s[6]]
                except Exception:
                    pass
                finally:
                    data.append(s)
            return render_template('systems.html', data=data, tcp_number=tcp_number, tcp_id=tcp_id)
        elif request.method == 'POST':
            tcp_id = int(request.args.get('tcp_id'))
            tcp_number = request.args.get('tcp_number')
            system_name = request.form.get('system_name')
            data = []
            with db_handler.connect_db() as connection:
                db_handler.create_config(tcp_id, system_name, 1, '', '', '', 0.0, '', connection)
                system = db_handler.get_tcp_configs((tcp_id, ), connection)
            for s in system:
                s = list(s)
                try:
                    s[6] = types[s[6]]
                except Exception:
                    pass
                finally:
                    data.append(s)
            return render_template('systems.html', data=data, tcp_number=tcp_number, tcp_id=tcp_id)
    else:
        return redirect(url_for('admin'))


@app.route("/systems_update", methods=['POST'])
def systems_update():
    tcp_id = request.args.get('tcp_id')
    tcp_number = request.args.get('tcp_number')
    if request.method == 'POST':
        receive_systems = request.args.get('systems')
        receive_systems = json.loads(receive_systems)
        with db_handler.connect_db() as connection:
            for r_sys in receive_systems:
                db_handler.update_quantity(receive_systems[r_sys], r_sys, connection)
    return redirect(url_for('systems', tcp_id=tcp_id, tcp_number=tcp_number))


@app.route("/tcps_update", methods=['POST'])
def tcps_update():
    if request.method == 'POST':
        receive_tcps = request.args.get('tcps')
        receive_tcps = json.loads(receive_tcps)
        with db_handler.connect_db() as connection:
            for r_tcp in receive_tcps:
                db_handler.update_status(receive_tcps[r_tcp], r_tcp, connection)
    return redirect(url_for('main'))


@app.route("/configurator", methods=['GET', 'POST'])
def configurator():
    try:
        user_name = session['user_name']
    except Exception:
        user_name = ''
    if user_name == 'admin' or user_name == 'user':
        global rate
        global rate_date
        difference = datetime.datetime.now() - rate_date
        if difference.total_seconds() > 86400:
            rate = get_rate()
            rate_date = datetime.datetime.now()
        system_id = request.args.get('id')
        with db_handler.connect_db() as connection:
            system = db_handler.get_config((int(system_id),), connection)
            tcp = db_handler.get_tcp((system[1], ), connection)
            if system[6] != '':
                system = {
                    'name': tcp[2],
                    'object': tcp[3],
                    'tcp': tcp[1],
                    'customer': tcp[4],
                    'executor': tcp[5],
                    'system_id': system[0],
                    'system_name': system[2],
                    'param': system[4],
                    'num_param': system[5],
                    'sys_type': system[6],
                    'status': 'custom'
                }
            else:
                system = {
                    'name': tcp[2],
                    'object': tcp[3],
                    'tcp': tcp[1],
                    'customer': tcp[4],
                    'executor': tcp[5],
                    'system_id': system[0],
                    'system_name': system[2],
                    'param': system[4],
                    'num_param': system[5],
                    'sys_type': system[6],
                    'status': 'default'
                }
            system = json.dumps(system)
            prev = [tcp[0], tcp[1]]
        return render_template('configurator.html', system=system, prev=prev)
    else:
        return redirect(url_for('admin'))


@app.route('/tables', methods=['GET', 'POST'])
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


@app.route('/table_data', methods=['GET', 'POST'])
def table_data():
    try:
        user_name = session['user_name']
    except Exception:
        user_name = ''
    if user_name == 'admin' or user_name == 'user':
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
                for i in range(1, 9):
                    row.append(request.form.getlist(str(i))[j])
                table_list.append(row)
            try:
                with db_handler.connect_db() as connection:
                    cursor = connection.cursor()
                    for row in table_list:
                        sql = f'''UPDATE `{table_name}`
                            SET `name`=%s, `manufacturer`=%s, `article`=%s, `parameter`=%s, `price`=%s, `groups`=%s, `code`=%s
                            WHERE `id` = %s;'''
                        cursor.execute(sql, [row[1], row[2], row[3], row[4], float(row[5]), row[6], row[7], int(row[0])])
                    connection.commit()
                flash("Записи обновлены")
            except Exception as e:
                print(str(e))
                flash("Ошибка ввода")
            return render_template('table_detail.html', table_list=table_list, table_name=table_name)
    else:
        return redirect(url_for('admin'))


@app.route('/systems_admin', methods=['GET'])
def systems_admin():
    try:
        user_name = session['user_name']
    except Exception:
        user_name = ''
    if user_name == 'admin' or user_name == 'user':
        if request.method == 'GET':
            with db_handler.connect_db() as connection:
                table_name = 'Tcp'
                cursor = connection.cursor()
                sql = f"SELECT * FROM {table_name};"
                cursor.execute(sql,)
                table_list = cursor.fetchall()
            return render_template('systems_admin.html', table_list=table_list, table_name=table_name)
    else:
        return redirect(url_for('admin'))


@app.route('/delete_tcp', methods=['GET'])
def delete_tcp():
    tcp_id = request.args.get('tcp_id')
    with db_handler.connect_db() as connection:
        cursor = connection.cursor()
        sql = f"DELETE FROM `Tcp` WHERE `id`=%s;"
        cursor.execute(sql, (tcp_id, ))
        connection.commit()
    return redirect(url_for('tables'))


@app.route('/specification.xlsx')
def download_file():
    query = request.args.get('data')
    query = json.loads(query)
    return send_file('specification.xlsx', download_name=f"Спецификация_{query['name']}_{str(datetime.date.today())}.xlsx")


@app.route('/TCP.xlsx')
def download_second_file():
    query = request.args.get('data')
    query = json.loads(query)
    date = datetime.date.today()
    add_tcp_name(query['name'], query['object'], query['number'], query['customer'], query['executor'], date)
    return send_file('TCP.xlsx', download_name=f"ТКП_{query['name']}_{str(datetime.date.today())}.xlsx")


@app.route('/schema.pdf')
def download_schema():
    query = request.args.get('data')
    query = json.loads(query)
    return send_file('schema.pdf', download_name=f"Схема_{query['name']}_{str(datetime.date.today())}.pdf")


@app.route('/elscheme')
def download_el_schema():
    query = request.args.get('data')
    query = json.loads(query)
    return send_file('static/scheme/'+query['path'], download_name=f"Схема_электрическая{query['name']}_{str(datetime.date.today())}.pdf")


@app.route('/general_tcp.xlsx')
def download_general_tcp():
    tcp_id = request.args.get('tcp_id')
    with db_handler.connect_db() as connection:
        tcp_configs = db_handler.get_tcp_configs((int(tcp_id), ), connection)
        tcp = db_handler.get_tcp((int(tcp_id), ), connection)
    tcp_data = {
        'company_name': tcp[2],
        'company_object': tcp[3],
        'executor': tcp[5],
        'customer': tcp[4],
        'tcp_number': tcp[1]
    }
    system_configs = []
    system_names = []
    quantitys = []
    for system in tcp_configs:
        quantitys.append(system[3])
        system_names.append(system[2])
        try:
            system_configs.append(json.loads(system[8]))
        except json.decoder.JSONDecodeError:
            pass
    create_general_tcp(system_configs, rate, system_names, tcp_data, quantitys)
    return send_file('general_tcp.xlsx', download_name=f"general_tcp.xlsx")


@sock.route('/configurator')
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
            price, signals = handler.calculate()
            receive_message['price'] = int(price * rate)
            receive_message['signals'] = signals
        elif 'get_exel' in new_message:
            receive_message = handler.create_docs(rate)
        elif 'command' in new_message:
            if new_message['command'] == 'save_config':
                parameters, num_parameters, system_type = handler.get_configuration()
                price, signals = handler.calculate()
                system_name = new_message['system_name']
                elements_list = json.dumps(handler.get_elements_list(), ensure_ascii=False, default=str)
                system_id = int(new_message['system_id'])
                with db_handler.connect_db() as connection:
                    db_handler.save_config(system_name, parameters, num_parameters, system_type, price*rate, elements_list, system_id, connection)
                receive_message['price'] = int(price * rate)
                receive_message['signals'] = signals
                receive_message['img_list'] = handler.img_list
        else:
            handler.add_parameters(new_message)
            price, signals = handler.calculate()
            receive_message['price'] = int(price * rate)
            receive_message['signals'] = signals
            receive_message['img_list'] = handler.img_list
            # print(receive_message['img_list'])
        receive_message = json.dumps(receive_message)
        sock.send(receive_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0')