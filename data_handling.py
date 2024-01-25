
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
        "res_out": 1000
    }

    def __init__(self):
        self.price = 0
        self.parameters = []
        self.system_type = None

    def add_parameters(self, message):
        for mes in message:
            if message[mes] == 'true':
                if mes not in self.parameters:
                    self.parameters.append(mes)
            elif message[mes] == 'false':
                if mes in self.parameters:
                    self.parameters.remove(mes)
        print(self.parameters)

    def add_type(self, new_type):
        self.system_type = new_type
        self.parameters = []

    def get_price(self, param):
        return self.price_data[param]

    def calculate(self):
        price = self.get_price(self.system_type)
        for param in self.parameters:
            price += self.get_price(param)
        return price



# message_data = {
#     "select_0": select_0,
#     "select_1": select_1,
#     "select_2": select_2,
#     "damp_in": damp_in,
#     "damp_out": damp_out,
#     "filt_in": filt_in,
#     "filt_out": filt_out,
#     "res_in": res_in,
#     "res_out": res_out
# }