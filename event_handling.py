import img_data
import db_handler


def vent_in(obj):
    if 'dif_in' in obj.parameters:
        if 'FC_in' in obj.parameters:
            if obj.system_type == 'In_out':
                if 'smooth_in' in obj.parameters:
                    key = '9'
                else:
                    key = '3'
            elif obj.system_type == "In":
                if 'smooth_in' in obj.parameters:
                    key = '11'
                else:
                    key = '7'
        else:
            if obj.system_type == 'In_out':
                key = '1'
            elif obj.system_type == "In":
                key = '5'
    else:
        if 'FC_in' in obj.parameters:
            if obj.system_type == 'In_out':
                if 'smooth_in' in obj.parameters:
                    key = '8'
                else:
                    key = '2'
            elif obj.system_type == "In":
                if 'smooth_in' in obj.parameters:
                    key = '10'
                else:
                    key = '6'
        else:
            if obj.system_type == 'In_out':
                key = '0'
            elif obj.system_type == "In":
                key = '4'
    if obj.system_type != 'Out':
        obj.img_list[9] = img_data.vent_in_img[key]
    return [0, [0, 0, 0, 0, 0], []]


def vent_out(obj):
    index = 10 if obj.system_type == 'In_out' else 2
    if 'dif_out' in obj.parameters:
        if 'FC_out' in obj.parameters:
            if obj.system_type == 'In_out':
                if 'smooth_out' in obj.parameters:
                    key = '9'
                else:
                    key = '3'
            elif obj.system_type == "Out":
                if 'smooth_out' in obj.parameters:
                    key = '11'
                else:
                    key = '7'
        else:
            if obj.system_type == 'In_out':
                key = '1'
            elif obj.system_type == "Out":
                key = '5'
    else:
        if 'FC_out' in obj.parameters:
            if obj.system_type == 'In_out':
                if 'smooth_out' in obj.parameters:
                    key = '8'
                else:
                    key = '2'
            elif obj.system_type == "Out":
                if 'smooth_out' in obj.parameters:
                    key = '10'
                else:
                    key = '6'
        else:
            if obj.system_type == 'In_out':
                key = '0'
            elif obj.system_type == "Out":
                key = '4'
    if obj.system_type != 'In':
        obj.img_list[index] = img_data.vent_out_img[key]
    return [0, [0, 0, 0, 0, 0], []]


def first_heater(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if 'select_0' not in obj.parameters:
        for i in range(0, 4):
            obj.img_list[i+4] = ''
    if obj.system_type == "In_out":
        if 'first_heater_type' not in obj.parameters and 'select_0' in obj.parameters:
            sign[4] += 1
            price += db_handler.contactor_price((1,), obj.data_base)
            spec.append(db_handler.contactor_obj((1, ), obj.data_base))
            if 'first_pump_voltage' in obj.parameters:
                price += db_handler.breaker_price((2,), obj.data_base)
                spec.append(db_handler.breaker_obj((2,), obj.data_base))
            else:
                price += db_handler.breaker_price((4,), obj.data_base)
                spec.append(db_handler.breaker_obj((4,), obj.data_base))
            sign[3] += 1
            sign[1] += 1
            price += db_handler.other_price((8,), obj.data_base)
            spec.append(db_handler.other_obj((8,), obj.data_base))
            if 'first_confirm' in obj.parameters:
                key = '0'
                sign[0] += 1
            elif 'first_confirm' not in obj.parameters:
                key = '1'
            if 'first_thermostat' in obj.parameters:
                obj.img_list[5] = img_data.heater_img['10']
                sign[0] += 1
                price += db_handler.other_price((9,), obj.data_base)
                spec.append(db_handler.other_obj((9,), obj.data_base))
            else:
                obj.img_list[5] = ''
        elif 'first_heater_type' in obj.parameters and 'select_0' in obj.parameters:
            obj.img_list[5] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '6', '4': '7'}
            if "first_steps" in obj.numer_param:
                if 'electrical_first_step_signal' not in obj.parameters:
                    if obj.numer_param['first_steps'] == '0':
                        sign[4] += 1
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']], ), obj.data_base)
                        spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base))
                        price += db_handler.breaker_price((1, ), obj.data_base)
                        spec.append(db_handler.breaker_obj((1, ), obj.data_base))
                    elif obj.numer_param['first_steps'] == '1':
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                            spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '2':
                        sign[4] += 3
                        for i in range(3):
                            price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                            spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                elif 'electrical_first_step_signal' in obj.parameters:
                    if obj.numer_param['first_steps'] == '0':
                        sign[3] += 1
                        price += db_handler.other_price((10,), obj.data_base)
                        price += db_handler.other_price((11,), obj.data_base)
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                        spec.append(db_handler.other_obj((10,), obj.data_base))
                        spec.append(db_handler.other_obj((11,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '1':
                        sign[3] += 1
                        sign[4] += 1
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                        spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base))
                        for i in range(2):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '2':
                        sign[3] += 1
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                            spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base))
                        for i in range(3):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
            if 'first_electrical_thermal' in obj.numer_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[obj.numer_param['first_electrical_thermal']]
                sign[0] += int(obj.numer_param['first_electrical_thermal'])
    elif obj.system_type == 'In':
        if 'first_heater_type' not in obj.parameters and 'select_0' in obj.parameters:
            sign[4] += 1
            price += db_handler.contactor_price((1,), obj.data_base)
            spec.append(db_handler.contactor_obj((1,), obj.data_base))
            if 'first_pump_voltage' in obj.parameters:
                price += db_handler.breaker_price((2,), obj.data_base)
                spec.append(db_handler.breaker_obj((2,), obj.data_base))
            else:
                price += db_handler.breaker_price((4,), obj.data_base)
                spec.append(db_handler.breaker_obj((4,), obj.data_base))
            sign[3] += 1
            sign[1] += 1
            price += db_handler.other_price((8,), obj.data_base)
            spec.append(db_handler.other_obj((8,), obj.data_base))
            if 'first_confirm' in obj.parameters:
                key = '5'
                sign[0] += 1
            elif 'first_confirm' not in obj.parameters:
                key = '6'
            if 'first_thermostat' in obj.parameters:
                obj.img_list[5] = img_data.heater_img['11']
                sign[0] += 1
                price += db_handler.other_price((9,), obj.data_base)
                spec.append(db_handler.other_obj((9,), obj.data_base))
            else:
                obj.img_list[5] = ''
        elif 'first_heater_type' in obj.parameters and 'select_0' in obj.parameters:
            obj.img_list[5] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '6', '4': '7'}
            if "first_steps" in obj.numer_param:
                if 'electrical_first_step_signal' not in obj.parameters:
                    if obj.numer_param['first_steps'] == '0':
                        sign[4] += 1
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '1':
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                         obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '2':
                        sign[4] += 3
                        for i in range(3):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                         obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                elif 'electrical_first_step_signal' in obj.parameters:
                    if obj.numer_param['first_steps'] == '0':
                        sign[3] += 1
                        price += db_handler.other_price((10,), obj.data_base)
                        price += db_handler.other_price((11,), obj.data_base)
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                        spec.append(db_handler.other_obj((10,), obj.data_base))
                        spec.append(db_handler.other_obj((11,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '1':
                        sign[3] += 1
                        sign[4] += 1
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                     obj.data_base))
                        for i in range(2):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['first_steps'] == '2':
                        sign[3] += 1
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                         obj.data_base))
                        for i in range(3):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
            if 'first_electrical_thermal' in obj.numer_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[obj.numer_param['first_electrical_thermal']]
    try:
        obj.img_list[4] = img_data.heater_img[key]
    except Exception:
        obj.img_list[4] = ''
    return [price, sign, spec]


def cooler(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == 'In_out':
        index = 6
        if 'select_1' in obj.parameters:
            sign[4] += 1
            if 'cool_alarm' in obj.parameters:
                key = '1'
                sign[0] += 1
            elif 'cool_alarm' not in obj.parameters:
                key = '0'
        else:
            key = '4'
    elif obj.system_type == 'In':
        index = 6
        if 'select_1' in obj.parameters:
            sign[4] += 1
            if 'cool_alarm' in obj.parameters:
                key = '3'
                sign[0] += 1
            elif 'cool_alarm' not in obj.parameters:
                key = '2'
        else:
            key = '4'
    if obj.system_type != 'Out':
        obj.img_list[index] = img_data.cooler_img[key]
    return [price, sign, spec]


def second_heater(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == "In_out":
        if 'second_heat_choice' in obj.parameters and 'second_heat_type' not in obj.parameters and 'select_0' in obj.parameters:
            sign[4] += 1
            price += db_handler.contactor_price((1,), obj.data_base)
            spec.append(db_handler.contactor_obj((1,), obj.data_base))
            if 'second_pump_voltage' in obj.parameters:
                price += db_handler.breaker_price((2,), obj.data_base)
                spec.append(db_handler.breaker_obj((2,), obj.data_base))
            else:
                price += db_handler.breaker_price((4,), obj.data_base)
                spec.append(db_handler.breaker_obj((4,), obj.data_base))
            sign[3] += 1
            if 'second_confirm' in obj.parameters and 'second_sensor' in obj.parameters:
                key = '0'
                sign[0] += 1
                sign[1] += 1
                price += db_handler.other_price((8,), obj.data_base)
                spec.append(db_handler.other_obj((8,), obj.data_base))
            elif 'second_confirm' not in obj.parameters and 'second_sensor' in obj.parameters:
                key = '1'
                sign[1] += 1
                price += db_handler.other_price((8,), obj.data_base)
                spec.append(db_handler.other_obj((8,), obj.data_base))
            elif 'second_confirm' not in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '14'
            elif 'second_confirm' in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '15'
                sign[0] += 1
            if 'second_thermostat' in obj.parameters:
                obj.img_list[8] = img_data.heater_img['10']
                sign[0] += 1
                price += db_handler.other_price((9,), obj.data_base)
                spec.append(db_handler.other_obj((9,), obj.data_base))
            else:
                obj.img_list[8] = ''
        elif 'second_heat_choice' in obj.parameters and 'second_heat_type' in obj.parameters and 'select_0' in obj.parameters:
            obj.img_list[8] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '6', '4': '7'}
            if "second_steps" in obj.numer_param:
                if 'electrical_second_step_signal' not in obj.parameters:
                    if obj.numer_param['second_steps'] == '0':
                        sign[4] += 1
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_second_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '1':
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                         obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '2':
                        sign[4] += 3
                        for i in range(3):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                         obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                elif 'electrical_second_step_signal' in obj.parameters:
                    if obj.numer_param['second_steps'] == '0':
                        sign[3] += 1
                        price += db_handler.other_price((10,), obj.data_base)
                        price += db_handler.other_price((11,), obj.data_base)
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                        spec.append(db_handler.other_obj((10,), obj.data_base))
                        spec.append(db_handler.other_obj((11,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '1':
                        sign[3] += 1
                        sign[4] += 1
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_second_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                     obj.data_base))
                        for i in range(2):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '2':
                        sign[3] += 1
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                         obj.data_base))
                        for i in range(3):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
            if 'second_electrical_thermal' in obj.numer_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[obj.numer_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in obj.parameters:
            key = '16'
            obj.img_list[8] = ''
    elif obj.system_type == 'In':
        if 'second_heat_choice' in obj.parameters and 'second_heat_type' not in obj.parameters and 'select_0' in obj.parameters:
            sign[4] += 1
            price += db_handler.contactor_price((1,), obj.data_base)
            spec.append(db_handler.contactor_obj((1,), obj.data_base))
            if 'second_pump_voltage' in obj.parameters:
                price += db_handler.breaker_price((2,), obj.data_base)
                spec.append(db_handler.breaker_obj((2,), obj.data_base))
            else:
                price += db_handler.breaker_price((4,), obj.data_base)
                spec.append(db_handler.breaker_obj((4,), obj.data_base))
            sign[3] += 1
            if 'second_confirm' in obj.parameters and 'second_sensor' in obj.parameters:
                key = '5'
                sign[0] += 1
                sign[1] += 1
                price += db_handler.other_price((8,), obj.data_base)
                spec.append(db_handler.other_obj((8,), obj.data_base))
            elif 'second_confirm' not in obj.parameters and 'second_sensor' in obj.parameters:
                key = '6'
                sign[1] += 1
                price += db_handler.other_price((8,), obj.data_base)
                spec.append(db_handler.other_obj((8,), obj.data_base))
            elif 'second_confirm' not in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '12'
            elif 'second_confirm' in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '13'
                sign[0] += 1
            if 'second_thermostat' in obj.parameters:
                obj.img_list[8] = img_data.heater_img['11']
                sign[0] += 1
                price += db_handler.other_price((9,), obj.data_base)
                spec.append(db_handler.other_obj((9,), obj.data_base))
            else:
                obj.img_list[8] = ''
        elif 'second_heat_choice' in obj.parameters and 'second_heat_type' in obj.parameters:
            obj.img_list[8] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '6', '4': '7'}
            if "second_steps" in obj.numer_param:
                if 'electrical_second_step_signal' not in obj.parameters:
                    if obj.numer_param['second_steps'] == '0':
                        sign[4] += 1
                        price += db_handler.contactor_price(
                            (variants[obj.numer_param['electrical_second_step_power']],),
                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '1':
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                         obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '2':
                        sign[4] += 3
                        for i in range(3):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                         obj.data_base))
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                elif 'electrical_second_step_signal' in obj.parameters:
                    if obj.numer_param['second_steps'] == '0':
                        sign[3] += 1
                        price += db_handler.other_price((10,), obj.data_base)
                        price += db_handler.other_price((11,), obj.data_base)
                        price += db_handler.breaker_price((1,), obj.data_base)
                        spec.append(db_handler.breaker_obj((1,), obj.data_base))
                        spec.append(db_handler.other_obj((10,), obj.data_base))
                        spec.append(db_handler.other_obj((11,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '1':
                        sign[3] += 1
                        sign[4] += 1
                        price += db_handler.contactor_price(
                            (variants[obj.numer_param['electrical_second_step_power']],),
                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                     obj.data_base))
                        for i in range(2):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
                    elif obj.numer_param['second_steps'] == '2':
                        sign[3] += 1
                        sign[4] += 2
                        for i in range(2):
                            price += db_handler.contactor_price(
                                (variants[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                            spec.append(
                                db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                         obj.data_base))
                        for i in range(3):
                            price += db_handler.breaker_price((1,), obj.data_base)
                            spec.append(db_handler.breaker_obj((1,), obj.data_base))
            if 'select_0' in obj.parameters and 'second_electrical_thermal' in obj.numer_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[obj.numer_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in obj.parameters:
            key = '16'
            obj.img_list[8] = ''
    try:
        obj.img_list[7] = img_data.heater_img[key]
    except Exception:
        obj.img_list[7] = ''
    return [price, sign, spec]


def dampers(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == "In_out":
        if 'damp_in' in obj.parameters:
            price += db_handler.relay_price(obj.data_base)
            for i in db_handler.relay_obj(obj.data_base):
                spec.append(i)
            sign[4] += 1
            if 'in_damper_confirm' in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '0'
                sign[0] += 1
                sign[4] += 1
                price += db_handler.breaker_price((5, ), obj.data_base)
                spec.append(db_handler.breaker_obj((5, ), obj.data_base))
                price += db_handler.contactor_price((1, ), obj.data_base)
                spec.append(db_handler.contactor_obj((1, ), obj.data_base))
            elif 'in_damper_confirm' in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '1'
                sign[0] += 1
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '2'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '3'
            obj.img_list[1] = img_data.dampers_img[key_in]
        else:
            obj.img_list[1] = ''
        if 'damp_out' in obj.parameters:
            price += db_handler.relay_price(obj.data_base)
            for i in db_handler.relay_obj(obj.data_base):
                spec.append(i)
            sign[4] += 1
            if 'out_damper_confirm' in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '4'
                sign[0] += 1
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '5'
                sign[0] += 1
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '6'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '7'
            obj.img_list[2] = img_data.dampers_img[key_out]
        else:
            obj.img_list[2] = ''
    elif obj.system_type == 'In':
        if 'damp_in' in obj.parameters:
            price += db_handler.relay_price(obj.data_base)
            for i in db_handler.relay_obj(obj.data_base):
                spec.append(i)
            sign[4] += 1
            if 'in_damper_confirm' in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '8'
                sign[0] += 1
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '9'
                sign[0] += 1
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '10'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '11'
            obj.img_list[1] = img_data.dampers_img[key_in]
        else:
            obj.img_list[1] = ''
    elif obj.system_type == 'Out':
        if 'damp_out' in obj.parameters:
            price += db_handler.relay_price(obj.data_base)
            for i in db_handler.relay_obj(obj.data_base):
                spec.append(i)
            sign[4] += 1
            if 'out_damper_confirm' in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '8'
                sign[0] += 1
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' in obj.parameters and 'otu_damper_heat' not in obj.parameters:
                key_out = '9'
                sign[0] += 1
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '10'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '11'
            obj.img_list[1] = img_data.dampers_img[key_out]
        else:
            obj.img_list[1] = ''
    return [price, sign, spec]


def filters(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == 'In_out':
        if 'filt_in' in obj.parameters:
            if 'in_filter_quantity' in obj.numer_param:
                variant = [3, 12, 13]
                for i in variant[:int(obj.numer_param['in_filter_quantity'])+1]:
                    obj.img_list[i] = img_data.filters_img['0']
                for i in variant[int(obj.numer_param['in_filter_quantity'])+1:]:
                    obj.img_list[i] = ''
                sign[0] += int(obj.numer_param['in_filter_quantity']) + 1
        elif "filt_in" not in obj.parameters:
            obj.img_list[3], obj.img_list[12], obj.img_list[13] = '', '', ''
        if 'filt_out' in obj.parameters:
            obj.img_list[11] = img_data.filters_img['1']
            sign[0] += 1
        elif 'filt_out' not in obj.parameters:
            obj.img_list[11] = ''
    elif obj.system_type == 'In':
        if 'filt_in' in obj.parameters:
            if 'in_filter_quantity' in obj.numer_param:
                variant = [3, 10, 11]
                for i in variant[:int(obj.numer_param['in_filter_quantity'])+1]:
                    obj.img_list[i] = img_data.filters_img['2']
                for i in variant[int(obj.numer_param['in_filter_quantity'])+1:]:
                    obj.img_list[i] = ''
                sign[0] += int(obj.numer_param['in_filter_quantity']) + 1
        elif "filt_in" not in obj.parameters:
            obj.img_list[3], obj.img_list[10], obj.img_list[11] = '', '', ''
    elif obj.system_type == 'Out':
        if 'filt_out' in obj.parameters:
            obj.img_list[3] = img_data.filters_img['2']
            sign[0] += 1
        else:
            obj.img_list[3] = ''
    return [price, sign, spec]


def cabinet(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    spec.append(db_handler.breaker_obj((5,), obj.data_base))
    price += db_handler.breaker_price((5,), obj.data_base)
    if obj.system_type == "In_out":
        if "switch_type" in obj.parameters:
            obj.img_list[18] = img_data.cabinet_img['1']
        else:
            obj.img_list[18] = img_data.cabinet_img['0']
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[14] = img_data.cabinet_img['2']
            sign[0] += 1
        else:
            obj.img_list[14] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            obj.img_list[0] = img_data.cabinet_img['4']
            sign[1] += 1
            price += db_handler.other_price((3,), obj.data_base)
            spec.append(db_handler.other_obj((3,), obj.data_base))
        else:
            obj.img_list[0] = img_data.cabinet_img['3']
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[21] = img_data.cabinet_img['6']
            sign[1] += 1
            price += db_handler.other_price((3,), obj.data_base)
            spec.append(db_handler.other_obj((3,), obj.data_base))
        else:
            obj.img_list[21] = img_data.cabinet_img['5']
        if 'sensor_humid' in obj.parameters:
            obj.img_list[19] = img_data.cabinet_img['7']
            sign[2] += 1
            price += db_handler.other_price((5,), obj.data_base)
            spec.append(db_handler.other_obj((5,), obj.data_base))
        else:
            obj.img_list[19] = ''
        if 'sensor_hood' in obj.parameters:
            obj.img_list[20] = img_data.cabinet_img['8']
            sign[1] += 1
            price += db_handler.other_price((2,), obj.data_base)
            spec.append(db_handler.other_obj((2,), obj.data_base))
        else:
            obj.img_list[20] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[15] = img_data.cabinet_img['9']
            sign[4] += 1
        else:
            obj.img_list[15] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[16] = img_data.cabinet_img['10']
            sign[4] += 1
        else:
            obj.img_list[16] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[17] = img_data.cabinet_img['11']
            sign[0] += 1
        else:
            obj.img_list[17] = ''
        if 'touchpad' in obj.parameters:
            price += db_handler.plc_price((6,), obj.data_base)
            spec.append(db_handler.plc_obj((6,), obj.data_base))
    elif obj.system_type == 'In':
        if "switch_type" in obj.parameters:
            obj.img_list[16] = img_data.cabinet_img['13']
        else:
            obj.img_list[16] = img_data.cabinet_img['12']
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[12] = img_data.cabinet_img['14']
            sign[0] += 1
        else:
            obj.img_list[12] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            obj.img_list[0] = img_data.cabinet_img['16']
            sign[1] += 1
            price += db_handler.other_price((3,), obj.data_base)
            spec.append(db_handler.other_obj((3,), obj.data_base))
        else:
            obj.img_list[0] = img_data.cabinet_img['15']
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[18] = img_data.cabinet_img['17']
            sign[1] += 1
            price += db_handler.other_price((3,), obj.data_base)
            spec.append(db_handler.other_obj((3,), obj.data_base))
        else:
            obj.img_list[18] = img_data.cabinet_img['18']
        if 'sensor_humid' in obj.parameters:
            obj.img_list[17] = img_data.cabinet_img['19']
            sign[2] += 1
            price += db_handler.other_price((5,), obj.data_base)
            spec.append(db_handler.other_obj((5,), obj.data_base))
        else:
            obj.img_list[17] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[13] = img_data.cabinet_img['20']
            sign[4] += 1
        else:
            obj.img_list[13] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[14] = img_data.cabinet_img['21']
            sign[4] += 1
        else:
            obj.img_list[14] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[15] = img_data.cabinet_img['22']
            sign[0] += 1
        else:
            obj.img_list[15] = ''
        if 'touchpad' in obj.parameters:
            price += db_handler.plc_price((6, ), obj.data_base)
            spec.append(db_handler.plc_obj((6, ), obj.data_base))
    elif obj.system_type == 'Out':
        if "switch_type" in obj.parameters:
            obj.img_list[8] = img_data.cabinet_img['13']
        else:
            obj.img_list[8] = img_data.cabinet_img['12']
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[4] = img_data.cabinet_img['14']
            sign[0] += 1
        else:
            obj.img_list[4] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            obj.img_list[0] = img_data.cabinet_img['16']
            sign[1] += 1
            price += db_handler.other_price((3,), obj.data_base)
            spec.append(db_handler.other_obj((3,), obj.data_base))
        else:
            obj.img_list[0] = img_data.cabinet_img['15']
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[10] = img_data.cabinet_img['17']
            sign[1] += 1
            price += db_handler.other_price((3,), obj.data_base)
            spec.append(db_handler.other_obj((3,), obj.data_base))
        else:
            obj.img_list[10] = img_data.cabinet_img['18']
        if 'sensor_hood' in obj.parameters:
            obj.img_list[9] = img_data.cabinet_img['8']
            sign[1] += 1
            price += db_handler.other_price((2,), obj.data_base)
            spec.append(db_handler.other_obj((2,), obj.data_base))
        else:
            obj.img_list[9] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[5] = img_data.cabinet_img['20']
            sign[4] += 1
        else:
            obj.img_list[5] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[6] = img_data.cabinet_img['21']
            sign[4] += 1
        else:
            obj.img_list[6] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[7] = img_data.cabinet_img['22']
            sign[0] += 1
        else:
            obj.img_list[7] = ''
        if 'touchpad' in obj.parameters:
            price += db_handler.plc_price((6, ), obj.data_base)
            spec.append(db_handler.plc_obj((6, ), obj.data_base))
    return [price, sign, spec]


def vent_power_in(obj):
    price = 0
    sign = [0, 0, 0, 0, 0]
    spec = []
    if obj.system_type != "Out":
        if int(obj.numer_param['vent_power_in']) <= 5:
            br_id = 3
        elif 5 < int(obj.numer_param['vent_power_in']) < 9:
            br_id = 2
        elif int(obj.numer_param['vent_power_in']) >= 9:
            br_id = 1
        breaker = db_handler.breaker_price((br_id,), obj.data_base)
        spec.append(db_handler.breaker_obj((br_id,), obj.data_base))
        breaker += db_handler.breaker_price((5,), obj.data_base)
        spec.append(db_handler.breaker_obj((5,), obj.data_base))
        if 'FC_in' in obj.parameters:
            power_price = db_handler.fc_price((int(obj.numer_param['vent_power_in']) + 1, ), obj.data_base)
            spec.append(db_handler.fc_obj((int(obj.numer_param['vent_power_in']) + 1,), obj.data_base))
            if 'smooth_in' in obj.parameters:
                sign[3] += 1
        else:
            if int(obj.numer_param['vent_power_in']) <= 8:
                cont_id = 1
            elif 8 < int(obj.numer_param['vent_power_in']) <= 14:
                cont_id = int(obj.numer_param['vent_power_in']) - 7
            else:
                cont_id = 7
            power_price = db_handler.contactor_price((cont_id, ), obj.data_base)
            spec.append(db_handler.contactor_obj((cont_id,), obj.data_base))
        if 'dif_in' in obj.parameters:
            dif = db_handler.diff_price(obj.data_base)
            dif += db_handler.relay_price(obj.data_base)
            spec.append(db_handler.diff_obj(obj.data_base))
            for i in db_handler.relay_obj(obj.data_base):
                spec.append(i)
            sign[0] += 1
        else:
            dif = 0
        relay = 2 * db_handler.relay_price(obj.data_base)
        for i in db_handler.relay_obj(obj.data_base):
            spec.append(i)
        for i in db_handler.relay_obj(obj.data_base):
            spec.append(i)
        price = power_price + dif + breaker + relay
    return [price, sign, spec]


def vent_power_out(obj):
    price = 0
    sign = [0, 0, 0, 0, 0]
    spec = []
    if obj.system_type != 'In':
        if int(obj.numer_param['vent_power_out']) <= 5:
            br_id = 3
        elif 5 < int(obj.numer_param['vent_power_out']) < 9:
            br_id = 2
        elif int(obj.numer_param['vent_power_out']) >= 9:
            br_id = 1
        breaker = db_handler.breaker_price((br_id,), obj.data_base)
        spec.append(db_handler.breaker_obj((br_id, ), obj.data_base))
        breaker += db_handler.breaker_price((5,), obj.data_base)
        spec.append(db_handler.breaker_obj((5,), obj.data_base))
        if 'FC_out' in obj.parameters:
            power_price = db_handler.fc_price((int(obj.numer_param['vent_power_out']) + 1, ), obj.data_base)
            spec.append(db_handler.fc_obj((int(obj.numer_param['vent_power_out']) + 1, ), obj.data_base))
            if 'smooth_out' in obj.parameters:
                sign[3] += 1
        else:
            if int(obj.numer_param['vent_power_out']) <= 8:
                cont_id = 1
            elif 8 < int(obj.numer_param['vent_power_out']) <= 14:
                cont_id = int(obj.numer_param['vent_power_out']) - 7
            else:
                cont_id = 7
            power_price = db_handler.contactor_price((cont_id, ), obj.data_base)
            spec.append(db_handler.contactor_obj((cont_id,), obj.data_base))
        if 'dif_out' in obj.parameters:
            dif = db_handler.diff_price(obj.data_base)
            dif += db_handler.relay_price(obj.data_base)
            spec.append(db_handler.diff_obj(obj.data_base))
            for i in db_handler.relay_obj(obj.data_base):
                spec.append(i)
            sign[0] += 1
        else:
            dif = 0
        relay = 2 * db_handler.relay_price(obj.data_base)
        for i in db_handler.relay_obj(obj.data_base):
            spec.append(i)
        for i in db_handler.relay_obj(obj.data_base):
            spec.append(i)
        price = power_price + dif + breaker + relay
    return [price, sign, spec]


def type_handling(system_type):
    if system_type == "In_out":
        return {"FC_in": "true", "FC_out": "true", "vent_power_in": '0', "vent_power_out": '0', 'shutdown_fire_signal': 'true'}
    elif system_type == "In":
        return {"FC_in": "true", "vent_power_in": '0', 'shutdown_fire_signal': 'true'}
    elif system_type == "Out":
        return {'FC_out': 'true', "vent_power_out": '0', 'shutdown_fire_signal': 'true'}


def add_static_elements(obj):
    data = db_handler.get_static_el(obj.data_base)
    data[0].insert(4, 1)
    data[1].insert(4, 1)
    data[2].insert(4, 1)
    data[3].insert(4, 300)
    data[4].insert(4, 100)
    data[5].insert(4, 100)
    data[6].insert(4, 100)
    data[7].insert(4, 4)
    data[8].insert(4, 4)
    data[9].insert(4, 2)
    data[10].insert(4, 1)
    data[11].insert(4, 2)
    data[12].insert(4, 1)
    data[13].insert(4, 1)

    for i, j in enumerate(data):
        summa = float(j[-1]) * j[-3]
        obj.price += summa
        data[i].append(summa)
    obj.static_elements = data

