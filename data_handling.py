from img_data import img_data
import event_handling
import create_specification
import db_handler


class Plc:
    def __init__(self, system_type):
        self.config = [1, 1, 0, 1, 1, 0]
        self.di = 3 if system_type == "In_out" else 2
        self.pt = 0
        self.ai = 0
        self.ao = 1
        self.do = 4 if system_type == "In_out" else 2

    def add_signals(self, di=0, pt=0, ai=0, ao=0, do=0):
        self.di += di
        self.pt += pt
        self.ai += ai
        self.ao += ao
        self.do += do
        self.config_plc()

    def config_plc(self):
        self.config[1] += self.di // 16
        self.config[2] += self.pt // 4
        self.config[3] += self.ai // 4 if self.ai // 4 >= self.ao // 4 else self.ao // 4
        self.config[4] += self.do // 8

    def get_plc_price(self, connection):
        price = db_handler.plc_price((1, ), connection)
        for i,j in enumerate(self.config[1:]):
            if j > 0:
                price += db_handler.plc_price((i+2, ), connection)
        print(self.di, self.do, self.ai, self.ao, self.pt)
        return price

    def get_spec_plc(self, connection):
        res = []
        for i,j in enumerate(self.config):
            for x in range(j):
                res.append(db_handler.plc_obj((i+1, ), connection))
        return res


class MessageHandler:
    price_data = {
        "select_0": event_handling.first_heater,
        "select_1": 1000,
        "select_2": 1000,
        "damp_in": event_handling.dampers,
        "damp_out": event_handling.dampers,
        "filt_in": event_handling.filters,
        "filt_out": event_handling.filters,
        "res_in": 1000,
        "res_out": 1000,
        "voltage_vent_in": 0,
        "voltage_vent_out": 0,
        "FC_in": event_handling.vent_in,
        "FC_out": event_handling.vent_out,
        "dif_in": event_handling.vent_in,
        "dif_out": event_handling.vent_out,
        "vent_power_in": {"0": event_handling.vent_power_in, "1": event_handling.vent_power_in, "2": event_handling.vent_power_in, "3": event_handling.vent_power_in, "4": event_handling.vent_power_in, "5": event_handling.vent_power_in, "6": event_handling.vent_power_in, "7": event_handling.vent_power_in, "8": event_handling.vent_power_in, "9": event_handling.vent_power_in, "10": event_handling.vent_power_in, "11": event_handling.vent_power_in, '12': event_handling.vent_power_in, '13': event_handling.vent_power_in, '14': event_handling.vent_power_in, '15': event_handling.vent_power_in, '16': event_handling.vent_power_in},
        "vent_power_out": {"0": event_handling.vent_power_out, "1": event_handling.vent_power_out, "2": event_handling.vent_power_out, "3": event_handling.vent_power_out, "4": event_handling.vent_power_out, "5": event_handling.vent_power_out, "6": event_handling.vent_power_out, "7": event_handling.vent_power_out, "8": event_handling.vent_power_out, "9": event_handling.vent_power_out, "10": event_handling.vent_power_out, "11": event_handling.vent_power_out, '12': event_handling.vent_power_out, '13': event_handling.vent_power_out, '14': event_handling.vent_power_out, '15': event_handling.vent_power_out, '16': event_handling.vent_power_out},
        "first_heater_type": event_handling.first_heater,
        "first_pump": 1000,
        "first_signal": 1000,
        "first_sensor": 1000,
        "first_thermostat": event_handling.first_heater,
        "first_pump_voltage": 1000,
        "first_valve_voltage": 1000,
        "first_confirm": event_handling.first_heater,
        "first_steps": {"0": 0, "1": 1000, "2": 2000},
        "electrical_first_step_power": {"0": 0, "1": 1000, "2": 2000, "3": 3000, "4": 4000, "5": 5000, "6": 6000, "7": 7000, "8": 8000, "9": 9000, "10": 10000, "11": 11000, "12": 12000},
        "electrical_first_step_signal": 1000,
        "first_electrical_thermal": {"0": 0, "1": 1000, "2": 2000},
        "second_heat_choice": event_handling.second_heater,
        "second_heat_type": event_handling.second_heater,
        "second_pump": 1000,
        "second_signal": 1000,
        "second_sensor": event_handling.second_heater,
        "second_thermostat": event_handling.second_heater,
        "second_pump_voltage": 1000,
        "second_valve_voltage": 1000,
        "second_confirm": event_handling.second_heater,
        "second_steps": {"0": 0, "1": 1000, "2": 2000},
        "electrical_second_step_power": {"0": 0, "1": 1000, "2": 2000, "3": 3000, "4": 4000, "5": 5000, "6": 6000, "7": 7000, "8": 8000, "9": 9000, "10": 10000, "11": 11000, "12": 12000},
        "electrical_second_step_signal": 1000,
        "second_electrical_thermal": {"0": 0, "1": 1000, "2": 2000},
        'in_damper_voltage': 1000,
        'in_damper_confirm': event_handling.dampers,
        'in_damper_heat': event_handling.dampers,
        'in_damper_heat_voltage': 1000,
        'in_damper_heat_power': {"0": 0, "1": 1000, "2": 2000, "3": 3000, "4": 4000, "5": 5000, "6": 6000, "7": 7000, "8": 8000, "9": 9000, "10": 10000, "11": 11000},
        'out_damper_voltage': 1000,
        'out_damper_confirm': event_handling.dampers,
        'out_damper_heat': event_handling.dampers,
        'out_damper_heat_voltage': 1000,
        'out_damper_heat_power': {"0": 0, "1": 1000, "2": 2000, "3": 3000, "4": 4000, "5": 5000, "6": 6000, "7": 7000, "8": 8000, "9": 9000, "10": 10000, "11": 11000},
        'in_filter_quantity': {"0": event_handling.filters, "1": event_handling.filters, "2": event_handling.filters},
        'out_filter_quantity': {"0": 0, "1": 1000, "2": 2000},
        'switch_type': event_handling.cabinet,
        'base_controller': {"0": 0, "1": 1000, "2": 2000},
        'shutdown_fire_signal': event_handling.cabinet,
        'sensor_temp_outdoor': event_handling.cabinet,
        'sensor_temp_indoor': event_handling.cabinet,
        'sensor_humid': event_handling.cabinet,
        'sensor_hood': event_handling.cabinet,
        'signal_work': event_handling.cabinet,
        'signal_alarm': event_handling.cabinet,
        'work_on_sched': 1000,
        'remote_control': event_handling.cabinet
    }

    def __init__(self):
        self.price = 0
        self.parameters = []
        self.numer_param = {}
        self.img_list = []
        self.system_type = None
        self.specification = []
        self.data_base = db_handler.connect_db()
        self.plc = None

    def __del__(self):
        self.data_base.close()

    def add_parameters(self, message):
        for mes in message:
            if message[mes] == 'true':
                if mes not in self.parameters:
                    self.parameters.append(mes)
            elif message[mes] == 'false':
                if mes in self.parameters:
                    self.parameters.remove(mes)
                    try:
                        self.price_data[mes](self)
                    except Exception:
                        pass
            else:
                self.numer_param[mes] = message[mes]

    def add_type(self, new_type):
        self.system_type = new_type
        self.parameters = []
        self.numer_param = {}
        self.img_list = img_data[new_type].copy()
        self.add_parameters(event_handling.type_handling(new_type))
        return self.img_list

    def get_price(self, param):
        print(self.parameters)
        print(self.numer_param)
        try:
            res = self.price_data[param](self)
            return res
        except Exception:
            res = self.price_data[param]
            return res

    def get_price_num(self, key, value):
        try:
            print(self.price_data[key][value])
            res = self.price_data[key][value](self)
            print(res)
            return res
        except Exception:
            return self.price_data[key][value]

    def calculate(self):
        self.specification = []
        self.plc = Plc(self.system_type)
        price = 0
        for param in self.parameters:
            price += self.get_price(param)
        for param in self.numer_param:
            price += self.get_price_num(param, self.numer_param[param])
        price += self.plc.get_plc_price(self.data_base)
        self.specification.extend(self.plc.get_spec_plc(self.data_base))
        print(self.specification)
        return price

    def create_exel(self):
        create_specification.create_exel(self.specification)
        return {"href": "specification.xlsx"}