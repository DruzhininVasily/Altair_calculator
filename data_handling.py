class PriceHandler:
    price_data = {
        "In_out": 3000000,
        "In": 2000000,
        "Out": 1000000,
        "select_0": 1000,
        "select_1": 1000,
        "select_2": 1000,
        "damp_in": 1000,
        "damp_out": 1000,
        "filt_in": 1000,
        "filt_out": 1000,
        "res_in": 1000,
        "res_out": 1000,
        "voltage_vent_in": 1000,
        "voltage_vent_out": 1000,
        "FC_in": 1000,
        "FC_out": 1000,
        "dif_in": 1000,
        "dif_out": 1000,
        "vent_power_in": {"0": 0, "1": 1000, "2": 2000, "3": 3000, "4": 4000, "5": 5000, "6": 6000, "7": 7000, "8": 8000, "9": 9000, "10": 10000, "11": 11000},
        "vent_power_out": {"0": 0, "1": 1000, "2": 2000, "3": 3000, "4": 4000, "5": 5000, "6": 6000, "7": 7000, "8": 8000, "9": 9000, "10": 10000, "11": 11000},
    }

    def __init__(self):
        self.price = 0
        self.parameters = []
        self.numer_param = {}
        self.system_type = None

    def add_parameters(self, message):
        for mes in message:
            if message[mes] == 'true':
                if mes not in self.parameters:
                    self.parameters.append(mes)
            elif message[mes] == 'false':
                if mes in self.parameters:
                    self.parameters.remove(mes)
            else:
                self.numer_param[mes] = message[mes]
                print(self.numer_param)
        print(self.parameters)

    def add_type(self, new_type):
        self.system_type = new_type
        self.parameters = []
        self.numer_param = {}

    def get_price(self, param):
        return self.price_data[param]

    def get_price_num(self, key, value):
        return self.price_data[key][value]

    def calculate(self):
        price = self.get_price(self.system_type)
        for param in self.parameters:
            price += self.get_price(param)
        for param in self.numer_param:
            price += self.get_price_num(param, self.numer_param[param])
        return price