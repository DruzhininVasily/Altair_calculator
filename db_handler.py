import mysql.connector


def connect_db():
    data_base = mysql.connector.connect(
        host='localhost',
        user="admin",
        password="Z1s2e3v4g5.",
        database="altair_materials"
        )
    return data_base


def fc_price(fc_id, connection):
    cursor = connection.cursor()
    sql = "SELECT price FROM FC WHERE id = %s"
    cursor.execute(sql, fc_id)
    res = float(cursor.fetchone()[0])
    return res


def fc_obj(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT name, manufacturer, article, parameter, price FROM FC WHERE id = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return res


def contactor_price(cont_id, connection):
    cursor = connection.cursor()
    sql = "SELECT price FROM contactors WHERE id = %s"
    cursor.execute(sql, cont_id)
    res = float(cursor.fetchone()[0])
    return res


def contactor_obj(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT name, manufacturer, article, parameter, price FROM contactors WHERE id = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return res


def diff_price(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT price FROM other WHERE id = 6')
    res = float(cursor.fetchone()[0])
    return res


def diff_obj(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name, manufacturer, article, parameter, price FROM other WHERE id = 6")
    res = cursor.fetchone()
    return res


def breaker_price(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT price FROM breakers WHERE id = %s"
    cursor.execute(sql, br_id)
    res = float(cursor.fetchone()[0])
    return res


def breaker_obj(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT name, manufacturer, article, parameter, price FROM breakers WHERE id = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return res


def relay_price(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT sum(price) FROM relay')
    res = float(cursor.fetchone()[0])
    return res


def relay_obj(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT  name, manufacturer, article, parameter, price FROM relay")
    res = cursor.fetchall()
    return res


def plc_price(plc_id, connection):
    cursor = connection.cursor()
    sql = "SELECT price FROM plc WHERE id = %s"
    cursor.execute(sql, plc_id)
    res = float(cursor.fetchone()[0])
    return res


def plc_obj(plc_id, connection):
    cursor = connection.cursor()
    sql = "SELECT name, manufacturer, article, parameter, price FROM plc WHERE id = %s"
    cursor.execute(sql, plc_id)
    res = cursor.fetchone()
    return res
