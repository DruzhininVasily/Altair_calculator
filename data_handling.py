def type_func(key):
    price = {
        "In_out": 3000000,
        "In": 2000000,
        "Out": 1000000
    }
    return price[key]


def select_0(value):
    if value == 'true':
        return 1000
    return 0


def select_1(value):
    if value == 'true':
        return 1000
    return 0


def select_2(value):
    if value == 'true':
        return 1000
    return 0


def damp_in(value):
    if value == 'true':
        return 1000
    return 0


def damp_out(value):
    if value == 'true':
        return 1000
    return 0


def filt_in(value):
    if value == 'true':
        return 1000
    return 0


def filt_out(value):
    if value == 'true':
        return 1000
    return 0


def res_in(value):
    if value == 'true':
        return 1000
    return 0


def res_out(value):
    if value == 'true':
        return 1000
    return 0


message_data = {
    "select_0": select_0,
    "select_1": select_1,
    "select_2": select_2,
    "damp_in": damp_in,
    "damp_out": damp_out,
    "filt_in": filt_in,
    "filt_out": filt_out,
    "res_in": res_in,
    "res_out": res_out
}