import mysql.connector


data_base = mysql.connector.connect(
    host='localhost',
    user="admin",
    password="Z1s2e3v4g5.",
    database="altair_materials"
    )


cursor = data_base.cursor()


def fc_price(fc_id):
    sql = "SELECT price FROM fc WHERE id = %s"
    cursor.execute(sql, fc_id)
    res = float(cursor.fetchone()[0])
    return res


def fc_obj(br_id):
    sql = "SELECT article, name, power, price FROM fc WHERE id = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return list(res)


def contactor_price(cont_id):
    sql = "SELECT price FROM contactors WHERE id = %s"
    cursor.execute(sql, cont_id)
    res = float(cursor.fetchone()[0])
    return res


def contactor_obj(br_id):
    sql = "SELECT manufacturer, article, current, price, purchase_price FROM contactors WHERE id = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return list(res)


def diff_price():
    cursor.execute('SELECT price FROM other WHERE id = 8')
    res = float(cursor.fetchone()[0])
    return res


def diff_obj():
    cursor.execute("SELECT name, article, price FROM other WHERE id = 8")
    res = cursor.fetchone()
    return list(res)


def breaker_price(br_id):
    sql = "SELECT price FROM breakers WHERE id = %s"
    cursor.execute(sql, br_id)
    res = float(cursor.fetchone()[0])
    return res


def breaker_obj(br_id):
    sql = "SELECT manufacturer, article, name, price, purchase_price FROM breakers WHERE id = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return list(res)


def relay_price():
    cursor.execute('SELECT sum(price) FROM relay')
    res = float(cursor.fetchone()[0])
    return res


def relay_obj():
    cursor.execute("SELECT  manufacturer, article, name, price, purchase_price FROM relay")
    res = cursor.fetchall()
    return res


def plc_price(plc_id):
    sql = "SELECT sum(price) FROM plc WHERE id <> %s"
    cursor.execute(sql, plc_id)
    res = float(cursor.fetchone()[0])
    return res
