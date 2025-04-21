from img_data import img_data
import event_handling
import create_specification
import db_handler
import json


class Plc:
    def __init__(self, system_type):
        self.config = [0, 0, 0, 0, 0, 0]
        self.di = 0
        self.pt = 0
        self.ai = 0
        self.ao = 0
        self.do = 0

    def add_signals(self, di=0, pt=0, ai=0, ao=0, do=0):
        self.di += di
        self.pt += pt
        self.ai += ai
        self.ao += ao
        self.do += do
        self.config_plc()

    def config_plc(self):
        self.config[0] = 1
        self.config[1] += 0 if self.di == 0 else (self.di // 16) + 1
        self.config[2] += 0 if self.pt == 0 else (self.pt // 4) + 1
        self.config[3] += 0 if self.ai == 0 and self.ao == 0 else (self.ai // 4) + 1 if self.ai // 4 >= self.ao // 4 else (self.ao // 4) + 1
        self.config[4] += 0 if self.do == 0 else (self.do // 8) + 1

    def get_plc_price(self, connection):
        price = db_handler.plc_price((1, ), connection)
        for i,j in enumerate(self.config[1:]):
            if j > 0:
                for x in range(j):
                    price += db_handler.plc_price((i+2, ), connection)
        # print(self.di, self.pt, self.ai, self.ao, self.do )
        return price

    def get_spec_plc(self, connection):
        res = []
        for i,j in enumerate(self.config):
            for x in range(j):
                res.append(db_handler.plc_obj((i+1, ), connection))
        return res

    def get_signals(self):
        return [self.di, self.do, self.ai, self.ao, self.pt]


class MessageHandler:

    FUNCTIONS = [event_handling.vent_in, event_handling.vent_out, event_handling.first_heater, event_handling.cooler,
                 event_handling.second_heater, event_handling.dampers, event_handling.filters,
                 event_handling.cabinet, event_handling.vent_power_in, event_handling.vent_power_out,
                 event_handling.get_panel, event_handling.humid]

    def __init__(self):
        self.price = 0
        self.parameters = []
        self.numer_param = {}
        self.img_list = []
        self.system_type = None
        self.specification = []
        self.data_base = db_handler.connect_db()
        self.plc = None
        self.static_elements = []

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
                    self.calculate()
            else:
                self.numer_param[mes] = message[mes]

    def add_type(self, new_type):
        self.system_type = new_type
        self.price = 0
        self.parameters = []
        self.numer_param = {}
        self.img_list = img_data[new_type].copy()
        self.add_parameters(event_handling.type_handling(new_type))
        event_handling.add_static_elements(self)
        return self.img_list

    def calculate(self):
        self.specification = []
        self.plc = Plc(self.system_type)
        price = self.price
        signals = [0, 0, 0, 0, 0]
        for func in self.FUNCTIONS:
            res_data = func(self)
            price += res_data[0]
            for i in range(len(signals)):
                signals[i] = signals[i] + res_data[1][i]
            self.specification.extend(res_data[2])
        self.plc.add_signals(di=signals[0], pt=signals[1], ai=signals[2], ao=signals[3], do=signals[4])
        price += self.plc.get_plc_price(self.data_base)
        self.specification.extend(self.plc.get_spec_plc(self.data_base))
        return price, self.plc.get_signals()

    def create_docs(self, rate):
        shau_name = create_specification.get_shau_name(self)
        create_specification.create_exel(self.specification, self.static_elements, rate, shau_name)
        create_specification.create_pdf(self.img_list)
        file_name = create_specification.get_scheme(self.system_type, self.parameters, self.numer_param)
        price, signals = self.calculate()
        return {"href": "specification.xlsx", 'href2': "TCP.xlsx", "href3": 'schema.pdf', 'href4': file_name, 'price': int(price*rate), 'signals': signals}

    def get_configuration(self):
        param_for_db = {}
        for param in self.parameters:
            param_for_db[param] = 'true'
        param_for_db = json.dumps(param_for_db)
        num_param_for_db = json.dumps(self.numer_param)
        sys_type = json.dumps({"type": self.system_type})
        return param_for_db, num_param_for_db, sys_type

    def get_elements_list(self):
        shau_name = create_specification.get_shau_name(self)
        return {'spec': self.specification, 'static': self.static_elements, 'shau_name': shau_name}
