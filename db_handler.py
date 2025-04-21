import mysql.connector
from dotenv import load_dotenv
import os


def connect_db():
    load_dotenv()
    data_base = mysql.connector.connect(
        host=os.getenv('SQL_HOST'),
        port=os.getenv('SQL_PORT'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PASS'),
        database=os.getenv('DATABASE')
        )
    return data_base


def create_tcp(name, comp_object, tcp, customer, executor, date, tcp_status, all_price, connection):
    cursor = connection.cursor()
    sql = "INSERT INTO `Tcp` (`tcp_number`, `organization`, `object`, `customer`, `executor`, `date`, `tcp_status`, `all_price`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (tcp, comp_object, name, customer, executor, date, tcp_status, all_price)
    cursor.execute(sql, val)
    connection.commit()


def get_tcp_configs(tcp_id, connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM `systems` WHERE `tcp` = %s"
    cursor.execute(sql, tcp_id)
    res = cursor.fetchall()
    return res


def get_all_tcp(connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM `Tcp`"
    cursor.execute(sql, )
    res = cursor.fetchall()
    return res


def get_tcp(tcp_id, connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM `Tcp` WHERE `id` = %s"
    cursor.execute(sql, tcp_id)
    res = cursor.fetchone()
    return res


def update_status(status, tcp_id, connection):
    cursor = connection.cursor()
    sql = "UPDATE `Tcp` SET `tcp_status`=%s WHERE id=%s;"
    val = (status, tcp_id)
    cursor.execute(sql, val)
    connection.commit()


def get_tcp_price(tcp_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price`, `quantity` FROM `systems` WHERE `tcp` = %s"
    cursor.execute(sql, tcp_id)
    res = cursor.fetchall()
    return res


def create_config(tcp, system_name, quantity, parameters, num_parameters, system_type, price, elements_list, connection):
    cursor = connection.cursor()
    sql = "INSERT INTO `systems` (`tcp`, `system_name`, `quantity`, `parameters`, `num_parameters`, `system_type`, `price`, `elements_list`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (tcp, system_name, quantity, parameters, num_parameters, system_type, price, elements_list)
    cursor.execute(sql, val)
    connection.commit()


def save_config(system_name, parameters, num_parameters, system_type, price, elements_list, system_id, connection):
    cursor = connection.cursor()
    sql = "UPDATE `systems` SET `system_name`=%s, `parameters`=%s, `num_parameters`=%s, `system_type`=%s, `price`=%s, `elements_list`=%s WHERE id=%s;"
    val = (system_name, parameters, num_parameters, system_type, price, elements_list, system_id)
    cursor.execute(sql, val)
    connection.commit()


def update_quantity(quantity, sys_id, connection):
    cursor = connection.cursor()
    sql = "UPDATE `systems` SET `quantity`=%s WHERE id=%s;"
    val = (quantity, sys_id)
    cursor.execute(sql, val)
    connection.commit()


def get_config(sys_id, connection):
    cursor = connection.cursor()
    sql = "SELECT * FROM `systems` WHERE `id` = %s"
    cursor.execute(sql, sys_id)
    res = cursor.fetchone()
    return res


def fc_price(fc_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `FC` WHERE `id` = %s"
    cursor.execute(sql, fc_id)
    res = float(cursor.fetchone()[0])
    return res


def fc_obj(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `FC` WHERE `id` = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return res


def contactor_price(cont_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `contactors` WHERE `id` = %s"
    cursor.execute(sql, cont_id)
    res = float(cursor.fetchone()[0])
    return res


def contactor_obj(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `contactors` WHERE `id` = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return res


def diff_price(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT `price` FROM `sensors` WHERE `id` = 4')
    res = float(cursor.fetchone()[0])
    return res


def diff_obj(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `sensors` WHERE `id` = 4")
    res = cursor.fetchone()
    return res


def breaker_price(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `breakers` WHERE `id` = %s"
    cursor.execute(sql, br_id)
    res = float(cursor.fetchone()[0])
    return res


def breaker_obj(br_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `breakers` WHERE `id` = %s"
    cursor.execute(sql, br_id)
    res = cursor.fetchone()
    return res


def relay_price(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT sum(`price`) FROM `relay` WHERE id < 3')
    res = float(cursor.fetchone()[0])
    return res


def relay_obj(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT  `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `relay` WHERE id < 3")
    res = cursor.fetchall()
    return res


def smooth_relay_price(smooth_id, connection):
    cursor = connection.cursor()
    sql = 'SELECT `price` FROM `relay` WHERE id = %s'
    cursor.execute(sql, smooth_id)
    res = float(cursor.fetchone()[0])
    return res


def smooth_relay_obj(smooth_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `relay` WHERE `id` = %s"
    cursor.execute(sql, smooth_id)
    res = cursor.fetchone()
    return res


def plc_price(plc_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `plc` WHERE `id` = %s"
    cursor.execute(sql, plc_id)
    res = float(cursor.fetchone()[0])
    return res


def plc_obj(plc_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `plc` WHERE `id` = %s"
    cursor.execute(sql, plc_id)
    res = cursor.fetchone()
    return res


def drive_price(drive_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `valve` WHERE `id` = %s"
    cursor.execute(sql, drive_id)
    res = float(cursor.fetchone()[0])
    return res


def drive_obj(drive_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `valve` WHERE `id` = %s"
    cursor.execute(sql, drive_id)
    res = cursor.fetchone()
    return res


def sensors_price(sens_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `sensors` WHERE `id` = %s"
    cursor.execute(sql, sens_id)
    res = float(cursor.fetchone()[0])
    return res


def sensors_obj(sens_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `sensors` WHERE `id` = %s"
    cursor.execute(sql, sens_id)
    res = cursor.fetchone()
    return res


def control_price(other_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `control` WHERE `id` = %s"
    cursor.execute(sql, other_id)
    res = float(cursor.fetchone()[0])
    return res


def control_obj(other_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `control` WHERE `id` = %s"
    cursor.execute(sql, other_id)
    res = cursor.fetchone()
    return res


def panel_price(panel_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `panels` WHERE `id` = %s"
    cursor.execute(sql, panel_id)
    res = float(cursor.fetchone()[0])
    return res


def panel_obj(panel_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `panels` WHERE `id` = %s"
    cursor.execute(sql, panel_id)
    res = cursor.fetchone()
    return res


def mont_elements_price(mont_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `price` FROM `mont_elements` WHERE `id` = %s"
    cursor.execute(sql, mont_id)
    res = float(cursor.fetchone()[0])
    return res


def mont_elements_obj(mont_id, connection):
    cursor = connection.cursor()
    sql = "SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `mont_elements` WHERE `id` = %s"
    cursor.execute(sql, mont_id)
    res = cursor.fetchone()
    return res


def get_static_el(connection):
    cursor = connection.cursor()
    sql = 'SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `cable` WHERE `id` > %s'
    cursor.execute(sql, (3, ))
    res = cursor.fetchall()
    for i, j in enumerate(res):
        res[i] = list(j)
    cursor.execute('SELECT `name`, `manufacturer`, `article`, `parameter`, `code`, `groups`, `price` FROM `mont_elements` WHERE `id` < 10')
    res1 = cursor.fetchall()
    for i, j in enumerate(res1):
        res1[i] = list(j)
    res.extend(res1)
    return res
