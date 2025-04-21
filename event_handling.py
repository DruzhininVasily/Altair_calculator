import img_data
import db_handler


def vent_in(obj):
    if obj.system_type != 'Out':
        if 'dif_in' in obj.parameters:
            if obj.numer_param["FC_in"] == "FC":
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
            elif obj.numer_param['FC_in'] == "NOT_FC":
                if obj.system_type == 'In_out':
                    key = '1'
                elif obj.system_type == "In":
                    key = '5'
            elif obj.numer_param['FC_in'] == 'EC':
                if obj.system_type == 'In_out':
                    key = '17'
                elif obj.system_type == 'In':
                    key = '13'
            elif obj.numer_param['FC_in'] == 'potentiometr':
                if obj.system_type == 'In_out':
                    key = '19'
                elif obj.system_type == 'In':
                    key = '15'
        else:
            if obj.numer_param["FC_in"] == "FC":
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
            elif obj.numer_param['FC_in'] == "NOT_FC":
                if obj.system_type == 'In_out':
                    key = '0'
                elif obj.system_type == "In":
                    key = '4'
            elif obj.numer_param['FC_in'] == 'EC':
                if obj.system_type == 'In_out':
                    key = '16'
                elif obj.system_type == 'In':
                    key = '12'
            elif obj.numer_param['FC_in'] == 'potentiometr':
                if obj.system_type == 'In_out':
                    key = '18'
                elif obj.system_type == 'In':
                    key = '14'
        quantity = 1
        if 'vent_quant_in' in obj.numer_param:
            quantity = int(obj.numer_param['vent_quant_in'])
        diff_quant = quantity
        if 'reserv_in' in obj.numer_param:
            if obj.numer_param['reserv_in'] != 'no_reserv':
                quantity += 1
            damp_indexes = [12, 14]
            if obj.numer_param['reserv_in'] == 'vent_reserv_in':
                if obj.system_type == 'In_out':
                    if 'vent_damp_confirm_in' in obj.parameters and 'vent_damp_heat_in' in obj.parameters:
                        damp_key = '0'
                    elif 'vent_damp_confirm_in' in obj.parameters and 'vent_damp_heat_in' not in obj.parameters:
                        damp_key = '1'
                    elif 'vent_damp_confirm_in' not in obj.parameters and 'vent_damp_heat_in' in obj.parameters:
                        damp_key = '2'
                    elif 'vent_damp_confirm_in' not in obj.parameters and 'vent_damp_heat_in' not in obj.parameters:
                        damp_key = '3'
                elif obj.system_type == 'In':
                    if 'vent_damp_confirm_in' in obj.parameters and 'vent_damp_heat_in' in obj.parameters:
                        damp_key = '8'
                    elif 'vent_damp_confirm_in' in obj.parameters and 'vent_damp_heat_in' not in obj.parameters:
                        damp_key = '9'
                    elif 'vent_damp_confirm_in' not in obj.parameters and 'vent_damp_heat_in' in obj.parameters:
                        damp_key = '10'
                    elif 'vent_damp_confirm_in' not in obj.parameters and 'vent_damp_heat_in' not in obj.parameters:
                        damp_key = '11'
                img_path = img_data.dampers_img[damp_key]
                if 'vent_damp_type_in' in obj.numer_param and int(obj.numer_param['vent_damp_type_in']) > 8:
                    img_path += '_analog'
                if obj.numer_param['damp_vent_quant_in'] == '2':
                    obj.img_list[damp_indexes[0]] = img_path + f'_x2.png'
                    obj.img_list[damp_indexes[1]] = ''
                elif obj.numer_param['damp_vent_quant_in'] == '4':
                    obj.img_list[damp_indexes[0]] = img_path + f'_x2.png'
                    obj.img_list[damp_indexes[1]] = img_path + f'_x2.png'
                else:
                    obj.img_list[damp_indexes[0]] = ''
                    obj.img_list[damp_indexes[1]] = ''
            elif obj.numer_param['reserv_in'] != 'vent_reserv_in':
                obj.img_list[damp_indexes[0]] = ''
                obj.img_list[damp_indexes[1]] = ''
        index = 13
        if 'reserv_in' in obj.numer_param:
            if obj.numer_param['reserv_in'] == 'vent_reserv_in' and 'quant_dif_in' in obj.numer_param:
                diff_quant = diff_quant + int(obj.numer_param['quant_dif_in']) - 1
        if 'dif_in' in obj.parameters:
            quant_str = f'_x{quantity}_x{diff_quant}.png'
        else:
            quant_str = f'_x{quantity}.png'
        obj.img_list[index] = img_data.vent_in_img[key] + quant_str
    return [0, [0, 0, 0, 0, 0], []]


def vent_out(obj):
    index = 16 if obj.system_type == 'In_out' else 4
    if obj.system_type != 'In':
        if 'dif_out' in obj.parameters:
            if obj.numer_param["FC_out"] == "FC":
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
            elif obj.numer_param['FC_out'] == "NOT_FC":
                if obj.system_type == 'In_out':
                    key = '1'
                elif obj.system_type == "Out":
                    key = '5'
            elif obj.numer_param['FC_out'] == 'EC':
                if obj.system_type == 'In_out':
                    key = '17'
                elif obj.system_type == 'Out':
                    key = '13'
            elif obj.numer_param['FC_out'] == 'potentiometr':
                if obj.system_type == 'In_out':
                    key = '19'
                elif obj.system_type == 'Out':
                    key = '15'
        else:
            if obj.numer_param["FC_out"] == "FC":
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
            elif obj.numer_param['FC_out'] == "NOT_FC":
                if obj.system_type == 'In_out':
                    key = '0'
                elif obj.system_type == "Out":
                    key = '4'
            elif obj.numer_param['FC_out'] == 'EC':
                if obj.system_type == 'In_out':
                    key = '16'
                elif obj.system_type == 'Out':
                    key = '12'
            elif obj.numer_param['FC_out'] == 'potentiometr':
                if obj.system_type == 'In_out':
                    key = '18'
                elif obj.system_type == 'Out':
                    key = '14'
        quantity = 1
        if 'vent_quant_out' in obj.numer_param:
            quantity = int(obj.numer_param['vent_quant_out'])
        diff_quant = quantity
        if 'reserv_out' in obj.numer_param:
            if obj.numer_param['reserv_out'] != 'no_reserv':
                quantity += 1
            if obj.system_type == 'In_out':
                damp_indexes = [15, 17]
            elif obj.system_type == 'Out':
                damp_indexes = [3, 5]
            if obj.numer_param['reserv_out'] == 'vent_reserv_out':
                if obj.system_type == 'In_out':
                    if 'vent_damp_confirm_out' in obj.parameters and 'vent_damp_heat_out' in obj.parameters:
                        damp_key = '4'
                    elif 'vent_damp_confirm_out' in obj.parameters and 'vent_damp_heat_out' not in obj.parameters:
                        damp_key = '5'
                    elif 'vent_damp_confirm_out' not in obj.parameters and 'vent_damp_heat_out' in obj.parameters:
                        damp_key = '6'
                    elif 'vent_damp_confirm_out' not in obj.parameters and 'vent_damp_heat_out' not in obj.parameters:
                        damp_key = '7'
                elif obj.system_type == 'Out':
                    if 'vent_damp_confirm_out' in obj.parameters and 'vent_damp_heat_out' in obj.parameters:
                        damp_key = '15'
                    elif 'vent_damp_confirm_out' in obj.parameters and 'vent_damp_heat_out' not in obj.parameters:
                        damp_key = '14'
                    elif 'vent_damp_confirm_out' not in obj.parameters and 'vent_damp_heat_out' in obj.parameters:
                        damp_key = '13'
                    elif 'vent_damp_confirm_out' not in obj.parameters and 'vent_damp_heat_out' not in obj.parameters:
                        damp_key = '12'
                img_path = img_data.dampers_img[damp_key]
                if 'vent_damp_type_out' in obj.numer_param and int(obj.numer_param['vent_damp_type_out']) > 8:
                    img_path += '_analog'
                if obj.numer_param['damp_vent_quant_out'] == '2':
                    obj.img_list[damp_indexes[0]] = img_path + f'_x2.png'
                    obj.img_list[damp_indexes[1]] = ''
                elif obj.numer_param['damp_vent_quant_out'] == '4':
                    obj.img_list[damp_indexes[0]] = img_path + f'_x2.png'
                    obj.img_list[damp_indexes[1]] = img_path + f'_x2.png'
                else:
                    obj.img_list[damp_indexes[0]] = ''
                    obj.img_list[damp_indexes[1]] = ''
            elif obj.numer_param['reserv_out'] != 'vent_reserv_out':
                obj.img_list[damp_indexes[0]] = ''
                obj.img_list[damp_indexes[1]] = ''
        if 'reserv_out' in obj.numer_param:
            if obj.numer_param['reserv_out'] == 'vent_reserv_out' and 'quant_dif_out' in obj.numer_param:
                diff_quant = diff_quant + int(obj.numer_param['quant_dif_out']) - 1
        if 'dif_out' in obj.parameters:
            quant_str = f'_x{quantity}_x{diff_quant}.png'
        else:
            quant_str = f'_x{quantity}.png'
        obj.img_list[index] = img_data.vent_out_img[key] + quant_str
    return [0, [0, 0, 0, 0, 0], []]


def first_heater(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if 'select_0' not in obj.parameters and obj.system_type != 'Out':
        for i in range(0, 4):
            obj.img_list[i+5] = ''
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
            sign[2] += 1
            price += db_handler.sensors_price((2,), obj.data_base)
            spec.append(db_handler.sensors_obj((2,), obj.data_base))
            key = '1'
            if 'first_thermostat' in obj.parameters:
                therm_id_s = [11, 12, 6, 7]
                therm_id = therm_id_s[0]
                if 'first_thermostat_length' in obj.numer_param:
                    therm_id = therm_id_s[int(obj.numer_param['first_thermostat_length'])-1]
                obj.img_list[6] = img_data.heater_img['10']
                therm_quant = 1
                if 'first_thermostat_quant' in obj.numer_param:
                    therm_quant = int(obj.numer_param['first_thermostat_quant'])
                for i in range(therm_quant):
                    sign[0] += 1
                    price += db_handler.sensors_price((therm_id,), obj.data_base)
                    spec.append(db_handler.sensors_obj((therm_id,), obj.data_base))
            else:
                obj.img_list[6] = ''
        elif 'first_heater_type' in obj.parameters and 'select_0' in obj.parameters:
            obj.img_list[6] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8'}
            variants_break = {'0': '16', '1': '17', '2': '18', '3': '19', '4': '20', '5': '21', '6': '22'}
            if "first_steps" in obj.numer_param:
                price += db_handler.breaker_price((1,), obj.data_base)
                spec.append(db_handler.breaker_obj((1,), obj.data_base))
                if 'electrical_first_step_signal' not in obj.parameters:
                    sign[4] += int(obj.numer_param['first_steps']) + 1
                    for i in range(int(obj.numer_param['first_steps']) + 1):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],),
                                                            obj.data_base)
                        spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],), obj.data_base))
                        price += db_handler.breaker_price((variants_break[obj.numer_param['electrical_first_step_power']], ), obj.data_base)
                        spec.append(db_handler.breaker_obj((variants_break[obj.numer_param['electrical_first_step_power']], ), obj.data_base))
                elif 'electrical_first_step_signal' in obj.parameters:
                    sign[3] += 1
                    price += db_handler.smooth_relay_price((3,), obj.data_base)
                    price += db_handler.smooth_relay_price((4,), obj.data_base)
                    price += db_handler.breaker_price((1,), obj.data_base)
                    sign[4] += int(obj.numer_param['first_steps'])
                    for i in range(int(obj.numer_param['first_steps'])):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_first_step_power']],),
                                                   obj.data_base))
            if 'first_electrical_thermal' in obj.numer_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                if obj.numer_param['first_electrical_thermal'] == '0' and 'electrical_first_step_signal' in obj.parameters:
                    key = '17'
                else:
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
            sign[2] += 1
            price += db_handler.sensors_price((2,), obj.data_base)
            spec.append(db_handler.sensors_obj((2,), obj.data_base))
            key = '13'
            if 'first_thermostat' in obj.parameters:
                therm_id_s = [11, 12, 6, 7]
                therm_id = therm_id_s[0]
                if 'first_thermostat_length' in obj.numer_param:
                    therm_id = therm_id_s[int(obj.numer_param['first_thermostat_length']) - 1]
                obj.img_list[6] = img_data.heater_img['11']
                therm_quant = 1
                if 'first_thermostat_quant' in obj.numer_param:
                    therm_quant = int(obj.numer_param['first_thermostat_quant'])
                for i in range(therm_quant):
                    sign[0] += 1
                    price += db_handler.sensors_price((therm_id,), obj.data_base)
                    spec.append(db_handler.sensors_obj((therm_id,), obj.data_base))
            else:
                obj.img_list[6] = ''
        elif 'first_heater_type' in obj.parameters and 'select_0' in obj.parameters:
            obj.img_list[6] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8'}
            variants_break = {'0': '16', '1': '17', '2': '18', '3': '19', '4': '20', '5': '21', '6': '22'}
            if "first_steps" in obj.numer_param:
                price += db_handler.breaker_price((1,), obj.data_base)
                spec.append(db_handler.breaker_obj((1,), obj.data_base))
                if 'electrical_first_step_signal' not in obj.parameters:
                    sign[4] += int(obj.numer_param['first_steps']) + 1
                    for i in range(int(obj.numer_param['first_steps']) + 1):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_first_step_power']],),
                                                   obj.data_base))
                elif 'electrical_first_step_signal' in obj.parameters:
                    sign[3] += 1
                    price += db_handler.smooth_relay_price((3,), obj.data_base)
                    price += db_handler.smooth_relay_price((4,), obj.data_base)
                    price += db_handler.breaker_price((1,), obj.data_base)
                    sign[4] += int(obj.numer_param['first_steps'])
                    for i in range(int(obj.numer_param['first_steps'])):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_first_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_first_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_first_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_first_step_power']],),
                                                   obj.data_base))
            if 'first_electrical_thermal' in obj.numer_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                if obj.numer_param['first_electrical_thermal'] == '0' and 'electrical_first_step_signal' in obj.parameters:
                    key = '18'
                else:
                    key = variant[obj.numer_param['first_electrical_thermal']]
    try:
        obj.img_list[5] = img_data.heater_img[key]
    except Exception:
        if obj.system_type != 'Out':
            obj.img_list[5] = ''
    return [price, sign, spec]


def cooler(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == 'In_out':
        index = 7
        if 'select_1' in obj.parameters:
            sign[3] += 1
            if obj.numer_param['cool_type'] == 'frion':
                if 'cool_alarm' in obj.parameters:
                    key = '1'
                    sign[0] += 1
                elif 'cool_alarm' not in obj.parameters:
                    key = '0'
            elif obj.numer_param['cool_type'] == 'water':
                key = '5'
        else:
            key = '4'
    elif obj.system_type == 'In':
        index = 7
        if 'select_1' in obj.parameters:
            sign[3] += 1
            if obj.numer_param['cool_type'] == 'frion':
                if 'cool_alarm' in obj.parameters:
                    key = '3'
                    sign[0] += 1
                elif 'cool_alarm' not in obj.parameters:
                    key = '2'
            elif obj.numer_param['cool_type'] == 'water':
                key = '6'
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
        if 'select_0' in obj.parameters and 'second_heat_choice' in obj.parameters and 'add_thermo_sensor' in obj.parameters:
            obj.img_list[8] = img_data.cabinet_img['34']
            sign[2] += 1
            price += db_handler.sensors_price((3,), obj.data_base)
            spec.append(db_handler.sensors_obj((3,), obj.data_base))
        else:
            obj.img_list[8] = ''
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
            if 'second_sensor' in obj.parameters:
                key = '1'
                sign[2] += 1
                price += db_handler.sensors_price((2,), obj.data_base)
                spec.append(db_handler.sensors_obj((2,), obj.data_base))
            elif 'second_sensor' not in obj.parameters:
                key = '14'
            if 'second_thermostat' in obj.parameters:
                therm_id_s = [11, 12, 6, 7]
                therm_id = therm_id_s[0]
                if 'second_thermostat_length' in obj.numer_param:
                    therm_id = therm_id_s[int(obj.numer_param['second_thermostat_length']) - 1]
                obj.img_list[10] = img_data.heater_img['10']
                therm_quant = 1
                if 'second_thermostat_quant' in obj.numer_param:
                    therm_quant = int(obj.numer_param['second_thermostat_quant'])
                for i in range(therm_quant):
                    sign[0] += 1
                    price += db_handler.sensors_price((therm_id,), obj.data_base)
                    spec.append(db_handler.sensors_obj((therm_id,), obj.data_base))
            else:
                obj.img_list[10] = ''
        elif 'second_heat_choice' in obj.parameters and 'second_heat_type' in obj.parameters and 'select_0' in obj.parameters:
            obj.img_list[9] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8'}
            variants_break = {'0': '16', '1': '17', '2': '18', '3': '19', '4': '20', '5': '21', '6': '22'}
            if "second_steps" in obj.numer_param:
                price += db_handler.breaker_price((1,), obj.data_base)
                spec.append(db_handler.breaker_obj((1,), obj.data_base))
                if 'electrical_second_step_signal' not in obj.parameters:
                    sign[4] += int(obj.numer_param['second_steps']) + 1
                    for i in range(int(obj.numer_param['second_steps']) + 1):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_second_step_power']],),
                                                            obj.data_base)
                        spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],), obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_second_step_power']],),
                                                   obj.data_base))
                elif 'electrical_second_step_signal' in obj.parameters:
                    sign[3] += 1
                    price += db_handler.smooth_relay_price((3,), obj.data_base)
                    price += db_handler.smooth_relay_price((4,), obj.data_base)
                    price += db_handler.breaker_price((1,), obj.data_base)
                    sign[4] += int(obj.numer_param['second_steps'])
                    for i in range(int(obj.numer_param['second_steps'])):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_second_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_second_step_power']],),
                                                   obj.data_base))
            if 'second_electrical_thermal' in obj.numer_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                if obj.numer_param['second_electrical_thermal'] == '0' and 'electrical_second_step_signal' in obj.parameters:
                    key = '17'
                else:
                    key = variant[obj.numer_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in obj.parameters:
            key = '16'
            obj.img_list[10] = ''
    elif obj.system_type == 'In':
        if 'select_0' in obj.parameters and 'second_heat_choice' in obj.parameters and 'add_thermo_sensor' in obj.parameters:
            obj.img_list[8] = img_data.cabinet_img['35']
            sign[2] += 1
            price += db_handler.sensors_price((3,), obj.data_base)
            spec.append(db_handler.sensors_obj((3,), obj.data_base))
        else:
            obj.img_list[8] = ''
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
            if 'second_sensor' in obj.parameters:
                key = '13'
                sign[2] += 1
                price += db_handler.sensors_price((2,), obj.data_base)
                spec.append(db_handler.sensors_obj((2,), obj.data_base))
            elif 'second_sensor' not in obj.parameters:
                key = '12'
            if 'second_thermostat' in obj.parameters:
                therm_id_s = [11, 12, 6, 7]
                therm_id = therm_id_s[0]
                if 'second_thermostat_length' in obj.numer_param:
                    therm_id = therm_id_s[int(obj.numer_param['second_thermostat_length']) - 1]
                obj.img_list[10] = img_data.heater_img['11']
                therm_quant = 1
                if 'second_thermostat_quant' in obj.numer_param:
                    therm_quant = int(obj.numer_param['second_thermostat_quant'])
                for i in range(therm_quant):
                    sign[0] += 1
                    price += db_handler.sensors_price((therm_id,), obj.data_base)
                    spec.append(db_handler.sensors_obj((therm_id,), obj.data_base))
            else:
                obj.img_list[10] = ''
        elif 'second_heat_choice' in obj.parameters and 'second_heat_type' in obj.parameters:
            obj.img_list[10] = ''
            variants = {'0': '1', '1': '3', '2': '4', '3': '5', '4': '6', '5': '7', '6': '8'}
            variants_break = {'0': '16', '1': '17', '2': '18', '3': '19', '4': '20', '5': '21', '6': '22'}
            if "second_steps" in obj.numer_param:
                price += db_handler.breaker_price((1,), obj.data_base)
                spec.append(db_handler.breaker_obj((1,), obj.data_base))
                if 'electrical_second_step_signal' not in obj.parameters:
                    sign[4] += int(obj.numer_param['second_steps']) + 1
                    for i in range(int(obj.numer_param['second_steps']) + 1):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_second_step_power']],),
                                                            obj.data_base)
                        spec.append(db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                             obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_second_step_power']],),
                                                   obj.data_base))
                elif 'electrical_second_step_signal' in obj.parameters:
                    sign[3] += 1
                    price += db_handler.smooth_relay_price((3,), obj.data_base)
                    price += db_handler.smooth_relay_price((4,), obj.data_base)
                    price += db_handler.breaker_price((1,), obj.data_base)
                    sign[4] += int(obj.numer_param['second_steps'])
                    for i in range(int(obj.numer_param['second_steps'])):
                        price += db_handler.contactor_price((variants[obj.numer_param['electrical_second_step_power']],),
                                                            obj.data_base)
                        spec.append(
                            db_handler.contactor_obj((variants[obj.numer_param['electrical_second_step_power']],),
                                                     obj.data_base))
                        price += db_handler.breaker_price(
                            (variants_break[obj.numer_param['electrical_second_step_power']],), obj.data_base)
                        spec.append(
                            db_handler.breaker_obj((variants_break[obj.numer_param['electrical_second_step_power']],),
                                                   obj.data_base))
            if 'select_0' in obj.parameters and 'second_electrical_thermal' in obj.numer_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                if obj.numer_param['second_electrical_thermal'] == '0' and 'electrical_second_step_signal' in obj.parameters:
                    key = '18'
                else:
                    key = variant[obj.numer_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in obj.parameters:
            key = '16'
            obj.img_list[10] = ''
    try:
        obj.img_list[9] = img_data.heater_img[key]
    except Exception:
        obj.img_list[9] = ''
    return [price, sign, spec]


def dampers(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == "In_out":
        if 'damp_in' in obj.parameters:
            if int(obj.numer_param['in_damper_type']) < 9:
                price += db_handler.relay_price(obj.data_base)
                for i in db_handler.relay_obj(obj.data_base):
                    spec.append(i)
                sign[4] += 1
            else:
                sign[3] += 1
            price += db_handler.drive_price((int(obj.numer_param['in_damper_type']) + 1, ), obj.data_base)
            spec.append(db_handler.drive_obj((int(obj.numer_param['in_damper_type']) + 1, ), obj.data_base))
            if 'in_damper_confirm' in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '0'
                sign[4] += 1
                if int(obj.numer_param['in_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '1'
                if int(obj.numer_param['in_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '2'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '3'
            if int(obj.numer_param['in_damper_type']) > 8:
                obj.img_list[2] = img_data.dampers_img[key_in] + '_analog.png'
            else:
                obj.img_list[2] = img_data.dampers_img[key_in] + '.png'
        else:
            obj.img_list[2] = ''
        if 'damp_out' in obj.parameters:
            if int(obj.numer_param['out_damper_type']) < 9:
                price += db_handler.relay_price(obj.data_base)
                for i in db_handler.relay_obj(obj.data_base):
                    spec.append(i)
                sign[4] += 1
            else:
                sign[3] += 1
            price += db_handler.drive_price((int(obj.numer_param['out_damper_type']) + 1,), obj.data_base)
            spec.append(db_handler.drive_obj((int(obj.numer_param['out_damper_type']) + 1,), obj.data_base))
            if 'out_damper_confirm' in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '4'
                sign[4] += 1
                if int(obj.numer_param['out_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '5'
                if int(obj.numer_param['out_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '6'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '7'
            if int(obj.numer_param['out_damper_type']) > 8:
                obj.img_list[3] = img_data.dampers_img[key_out] + '_analog.png'
            else:
                obj.img_list[3] = img_data.dampers_img[key_out] + '.png'
        else:
            obj.img_list[3] = ''
    elif obj.system_type == 'In':
        if 'damp_in' in obj.parameters:
            if int(obj.numer_param['in_damper_type']) < 9:
                price += db_handler.relay_price(obj.data_base)
                for i in db_handler.relay_obj(obj.data_base):
                    spec.append(i)
                sign[4] += 1
            else:
                sign[3] += 1
            price += db_handler.drive_price((int(obj.numer_param['in_damper_type']) + 1,), obj.data_base)
            spec.append(db_handler.drive_obj((int(obj.numer_param['in_damper_type']) + 1,), obj.data_base))
            if 'in_damper_confirm' in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '8'
                sign[4] += 1
                if int(obj.numer_param['in_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '9'
                if int(obj.numer_param['in_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '10'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '11'
            if int(obj.numer_param['in_damper_type']) > 8:
                obj.img_list[2] = img_data.dampers_img[key_in] + '_analog.png'
            else:
                obj.img_list[2] = img_data.dampers_img[key_in] + '.png'
        else:
            obj.img_list[2] = ''
    elif obj.system_type == 'Out':
        if 'damp_out' in obj.parameters:
            if int(obj.numer_param['out_damper_type']) < 9:
                price += db_handler.relay_price(obj.data_base)
                for i in db_handler.relay_obj(obj.data_base):
                    spec.append(i)
                sign[4] += 1
            else:
                sign[3] += 1
            price += db_handler.drive_price((int(obj.numer_param['out_damper_type']) + 1,), obj.data_base)
            spec.append(db_handler.drive_obj((int(obj.numer_param['out_damper_type']) + 1,), obj.data_base))
            if 'out_damper_confirm' in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '15'
                sign[4] += 1
                if int(obj.numer_param['out_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '14'
                if int(obj.numer_param['out_damper_type']) < 9:
                    sign[0] += 1
                else:
                    sign[2] += 1
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '13'
                sign[4] += 1
                price += db_handler.breaker_price((5,), obj.data_base)
                spec.append(db_handler.breaker_obj((5,), obj.data_base))
                price += db_handler.contactor_price((1,), obj.data_base)
                spec.append(db_handler.contactor_obj((1,), obj.data_base))
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '12'
            if int(obj.numer_param['out_damper_type']) > 8:
                obj.img_list[2] = img_data.dampers_img[key_out] + '_analog.png'
            else:
                obj.img_list[2] = img_data.dampers_img[key_out] + '.png'
        else:
            obj.img_list[2] = ''
    return [price, sign, spec]


def filters(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type == 'In_out':
        if 'filt_in' in obj.parameters:
            if 'filt_in_indication' in obj.parameters:
                quant = int(obj.numer_param['in_filter_quantity']) + 1
                if 'in_hepa_filter' in obj.parameters:
                    quant += 1
                sign[4] += quant
                price += db_handler.mont_elements_price((10,), obj.data_base) * quant
                for i in range(quant):
                    spec.append(db_handler.mont_elements_obj((10,), obj.data_base))
                obj.img_list[22] = img_data.filters_img['8'] + f"_x{quant}.png"
            else:
                obj.img_list[22] = ''
            if 'in_hepa_filter' in obj.parameters:
                sign[0] += 1
                price += db_handler.sensors_price((5,), obj.data_base)
                spec.append(db_handler.sensors_obj((5,), obj.data_base))
                obj.img_list[21] = img_data.filters_img['5']
            else:
                obj.img_list[21] = ''
            obj.img_list[4] = img_data.filters_img['0'] + f'_x1.png'
            if 'in_filter_quantity' in obj.numer_param:
                sign[0] += int(obj.numer_param['in_filter_quantity']) + 1
                for i in range(int(obj.numer_param['in_filter_quantity']) + 1):
                    price += db_handler.sensors_price((4,), obj.data_base)
                    spec.append(db_handler.sensors_obj((4,), obj.data_base))
                if int(obj.numer_param['in_filter_quantity']) > 0:
                    obj.img_list[20] = img_data.filters_img['0'] + f"_x{int(obj.numer_param['in_filter_quantity'])}.png"
                else:
                    obj.img_list[20] = ''
            else:
                obj.img_list[20] = ''
        elif "filt_in" not in obj.parameters:
            obj.img_list[4], obj.img_list[20], obj.img_list[21], obj.img_list[22] = '', '', '', ''
        if 'filt_out' in obj.parameters:
            quant = 1
            if 'out_filter_quantity' in obj.numer_param:
                quant += int(obj.numer_param['out_filter_quantity'])
            for i in range(quant):
                price += db_handler.sensors_price((4,), obj.data_base)
                spec.append(db_handler.sensors_obj((4,), obj.data_base))
                sign[0] += 1
            obj.img_list[19] = img_data.filters_img['1'] + f"_x{quant}.png"
            if 'filt_out_indication' in obj.parameters:
                if 'out_hepa_filter' in obj.parameters:
                    quant += 1
                sign[4] += quant
                price += db_handler.mont_elements_price((10,), obj.data_base) * quant
                for i in range(quant):
                    spec.append(db_handler.mont_elements_obj((10,), obj.data_base))
                obj.img_list[23] = img_data.filters_img['8'] + f"_x{quant}.png"
            else:
                obj.img_list[23] = ''
            if 'out_hepa_filter' in obj.parameters:
                sign[0] += 1
                price += db_handler.sensors_price((5,), obj.data_base)
                spec.append(db_handler.sensors_obj((5,), obj.data_base))
                obj.img_list[18] = img_data.filters_img['6']
            else:
                obj.img_list[18] = ''
        elif 'filt_out' not in obj.parameters:
            obj.img_list[18] = ''
            obj.img_list[19] = ''
            obj.img_list[23] = ''
    elif obj.system_type == 'In':
        if 'filt_in' in obj.parameters:
            if 'filt_in_indication' in obj.parameters:
                quant = int(obj.numer_param['in_filter_quantity']) + 1
                if 'in_hepa_filter' in obj.parameters:
                    quant += 1
                sign[4] += quant
                price += db_handler.mont_elements_price((10,), obj.data_base) * quant
                for i in range(quant):
                    spec.append(db_handler.mont_elements_obj((10,), obj.data_base))
                obj.img_list[17] = img_data.filters_img['9'] + f"_x{quant}.png"
            else:
                obj.img_list[17] = ''
            if 'in_hepa_filter' in obj.parameters:
                sign[0] += 1
                price += db_handler.sensors_price((5,), obj.data_base)
                spec.append(db_handler.sensors_obj((5,), obj.data_base))
                obj.img_list[16] = img_data.filters_img['4']
            else:
                obj.img_list[16] = ''
            if 'in_filter_quantity' in obj.numer_param:
                obj.img_list[4] = img_data.filters_img['2'] + f'_x1.png'
                if 'in_filter_quantity' in obj.numer_param:
                    sign[0] += int(obj.numer_param['in_filter_quantity']) + 1
                    for i in range(int(obj.numer_param['in_filter_quantity']) + 1):
                        price += db_handler.sensors_price((4,), obj.data_base)
                        spec.append(db_handler.sensors_obj((4,), obj.data_base))
                    if int(obj.numer_param['in_filter_quantity']) > 0:
                        obj.img_list[15] = img_data.filters_img[
                                               '2'] + f"_x{int(obj.numer_param['in_filter_quantity'])}.png"
                    else:
                        obj.img_list[15] = ''
                else:
                    obj.img_list[15] = ''
        elif "filt_in" not in obj.parameters:
            obj.img_list[4], obj.img_list[15], obj.img_list[16], obj.img_list[17] = '', '', '', ''
    elif obj.system_type == 'Out':
        if 'filt_out' in obj.parameters:
            quant = 1
            if 'out_filter_quantity' in obj.numer_param:
                quant += int(obj.numer_param['out_filter_quantity'])
            for i in range(quant):
                price += db_handler.sensors_price((4,), obj.data_base)
                spec.append(db_handler.sensors_obj((4,), obj.data_base))
                sign[0] += 1
            obj.img_list[7] = img_data.filters_img['3'] + f"_x{quant}.png"
            if 'filt_out_indication' in obj.parameters:
                if 'out_hepa_filter' in obj.parameters:
                    quant += 1
                sign[4] += quant
                price += db_handler.mont_elements_price((10,), obj.data_base) * quant
                for i in range(quant):
                    spec.append(db_handler.mont_elements_obj((10,), obj.data_base))
                obj.img_list[8] = img_data.filters_img['10'] + f"_x{quant}.png"
            else:
                obj.img_list[8] = ''
            if 'out_hepa_filter' in obj.parameters:
                sign[0] += 1
                price += db_handler.sensors_price((5,), obj.data_base)
                spec.append(db_handler.sensors_obj((5,), obj.data_base))
                obj.img_list[6] = img_data.filters_img['7']
            else:
                obj.img_list[6] = ''
        elif 'filt_out' not in obj.parameters:
            obj.img_list[6] = ''
            obj.img_list[7] = ''
            obj.img_list[8] = ''
    return [price, sign, spec]


def humid(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    if obj.system_type != 'Out':
        if obj.system_type == "In_out":
            if 'select_2' in obj.parameters:
                sign[3] += 1
                if 'humid_alarm' in obj.parameters:
                    sign[0] += 1
                    obj.img_list[11] = img_data.humid_img['3']
                else:
                    obj.img_list[11] = img_data.humid_img['2']
            else:
                obj.img_list[11] = ''
        elif obj.system_type == "In":
            if 'select_2' in obj.parameters:
                sign[3] += 1
                if 'humid_alarm' in obj.parameters:
                    sign[0] += 1
                    obj.img_list[11] = img_data.humid_img['1']
                else:
                    obj.img_list[11] = img_data.humid_img['0']
            else:
                obj.img_list[11] = ''
    return [price, sign, spec]


def cabinet(obj):
    spec = []
    price = 0
    sign = [0, 0, 0, 0, 0]
    spec.append(db_handler.breaker_obj((5,), obj.data_base))
    price += db_handler.breaker_price((5,), obj.data_base)
    if 'add_signals' in obj.parameters:
        add_sig = [obj.numer_param['di_signal'], obj.numer_param['pt_signal'], obj.numer_param['ai_signal'], obj.numer_param['ao_signal'], obj.numer_param['do_signal']]
        for i in range(len(add_sig)):
            if not add_sig[i].isdigit():
                add_sig[i] = '0'
            sign[i] += int(add_sig[i])
    if obj.system_type == "In_out":
        if "switch_type" in obj.parameters:
            obj.img_list[28] = img_data.cabinet_img['1']
            sign[0] += 1
        else:
            obj.img_list[28] = img_data.cabinet_img['0']
            sign[0] += 1
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[24] = img_data.cabinet_img['2']
            sign[0] += 1
        else:
            obj.img_list[24] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            if obj.numer_param['disp_protocol'] == '1':
                if obj.numer_param['sensor_temp_outdoor_type'] == 'chanel':
                    obj.img_list[1] = img_data.cabinet_img['34']
                    obj.img_list[0] = img_data.cabinet_img['3']
                    price += db_handler.sensors_price((3,), obj.data_base)
                    spec.append(db_handler.sensors_obj((3,), obj.data_base))
                elif obj.numer_param['sensor_temp_outdoor_type'] == 'outdoor':
                    obj.img_list[0] = img_data.cabinet_img['4']
                    obj.img_list[1] = ''
                    price += db_handler.sensors_price((1,), obj.data_base)
                    spec.append(db_handler.sensors_obj((1,), obj.data_base))
            elif obj.numer_param['disp_protocol'] == '2':
                if obj.numer_param['sensor_temp_outdoor_type'] == 'chanel':
                    obj.img_list[1] = img_data.cabinet_img['34']
                    obj.img_list[0] = img_data.cabinet_img['40']
                    price += db_handler.sensors_price((3,), obj.data_base)
                    spec.append(db_handler.sensors_obj((3,), obj.data_base))
                elif obj.numer_param['sensor_temp_outdoor_type'] == 'outdoor':
                    obj.img_list[0] = img_data.cabinet_img['41']
                    obj.img_list[1] = ''
                    price += db_handler.sensors_price((1,), obj.data_base)
                    spec.append(db_handler.sensors_obj((1,), obj.data_base))
            sign[2] += 1
        else:
            if 'disp_protocol' in obj.numer_param and obj.numer_param['disp_protocol'] == '2':
                obj.img_list[0] = img_data.cabinet_img['40']
                obj.img_list[1] = ''
            else:
                obj.img_list[0] = img_data.cabinet_img['3']
                obj.img_list[1] = ''
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[32] = img_data.cabinet_img['6']
            sign[2] += 1
            price += db_handler.sensors_price((9,), obj.data_base)
            spec.append(db_handler.sensors_obj((9,), obj.data_base))
        else:
            obj.img_list[32] = img_data.cabinet_img['5']
        if 'sensor_humid' in obj.parameters:
            obj.img_list[29] = img_data.cabinet_img['7']
            sign[2] += 1
            price += db_handler.sensors_price((8,), obj.data_base)
            spec.append(db_handler.sensors_obj((8,), obj.data_base))
        else:
            obj.img_list[29] = ''
        if 'sensor_hood_out' in obj.parameters:
            obj.img_list[30] = img_data.cabinet_img['8']
            sign[2] += 1
            price += db_handler.sensors_price((3,), obj.data_base)
            spec.append(db_handler.sensors_obj((3,), obj.data_base))
        else:
            obj.img_list[30] = ''
        if 'sensor_hood_in' in obj.parameters:
            obj.img_list[31] = img_data.cabinet_img['34']
            sign[2] += 1
            price += db_handler.sensors_price((3,), obj.data_base)
            spec.append(db_handler.sensors_obj((3,), obj.data_base))
        else:
            obj.img_list[31] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[25] = img_data.cabinet_img['9']
            sign[4] += 1
        else:
            obj.img_list[25] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[26] = img_data.cabinet_img['10']
            sign[4] += 1
        else:
            obj.img_list[26] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[27] = img_data.cabinet_img['11']
            sign[0] += 1
        else:
            obj.img_list[27] = ''
        if 'touchpad' in obj.parameters:
            price += db_handler.plc_price((6,), obj.data_base)
            spec.append(db_handler.plc_obj((6,), obj.data_base))
    elif obj.system_type == 'In':
        if "switch_type" in obj.parameters:
            obj.img_list[22] = img_data.cabinet_img['13']
            sign[0] += 1
        else:
            obj.img_list[22] = img_data.cabinet_img['12']
            sign[0] += 1
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[18] = img_data.cabinet_img['14']
            sign[0] += 1
        else:
            obj.img_list[18] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            if obj.numer_param['disp_protocol'] == '1':
                if obj.numer_param['sensor_temp_outdoor_type'] == 'chanel':
                    obj.img_list[1] = img_data.cabinet_img['35']
                    obj.img_list[0] = img_data.cabinet_img['15']
                    price += db_handler.sensors_price((3,), obj.data_base)
                    spec.append(db_handler.sensors_obj((3,), obj.data_base))
                elif obj.numer_param['sensor_temp_outdoor_type'] == 'outdoor':
                    obj.img_list[0] = img_data.cabinet_img['16']
                    obj.img_list[1] = ''
                    price += db_handler.sensors_price((1,), obj.data_base)
                    spec.append(db_handler.sensors_obj((1,), obj.data_base))
            elif obj.numer_param['disp_protocol'] == '2':
                if obj.numer_param['sensor_temp_outdoor_type'] == 'chanel':
                    obj.img_list[1] = img_data.cabinet_img['35']
                    obj.img_list[0] = img_data.cabinet_img['38']
                    price += db_handler.sensors_price((3,), obj.data_base)
                    spec.append(db_handler.sensors_obj((3,), obj.data_base))
                elif obj.numer_param['sensor_temp_outdoor_type'] == 'outdoor':
                    obj.img_list[0] = img_data.cabinet_img['39']
                    obj.img_list[1] = ''
                    price += db_handler.sensors_price((1,), obj.data_base)
                    spec.append(db_handler.sensors_obj((1,), obj.data_base))
            sign[2] += 1
        else:
            if 'disp_protocol' in obj.numer_param and obj.numer_param['disp_protocol'] == '2':
                obj.img_list[0] = img_data.cabinet_img['38']
                obj.img_list[1] = ''
            else:
                obj.img_list[0] = img_data.cabinet_img['15']
                obj.img_list[1] = ''
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[25] = img_data.cabinet_img['17']
            sign[2] += 1
            price += db_handler.sensors_price((9,), obj.data_base)
            spec.append(db_handler.sensors_obj((9,), obj.data_base))
        else:
            obj.img_list[25] = img_data.cabinet_img['18']
        if 'sensor_humid' in obj.parameters:
            obj.img_list[23] = img_data.cabinet_img['19']
            sign[2] += 1
            price += db_handler.sensors_price((8,), obj.data_base)
            spec.append(db_handler.sensors_obj((8,), obj.data_base))
        else:
            obj.img_list[23] = ''
        if 'sensor_hood_in' in obj.parameters:
            obj.img_list[24] = img_data.cabinet_img['35']
            sign[2] += 1
            price += db_handler.sensors_price((3,), obj.data_base)
            spec.append(db_handler.sensors_obj((3,), obj.data_base))
        else:
            obj.img_list[24] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[19] = img_data.cabinet_img['20']
            sign[4] += 1
        else:
            obj.img_list[19] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[20] = img_data.cabinet_img['21']
            sign[4] += 1
        else:
            obj.img_list[20] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[21] = img_data.cabinet_img['22']
            sign[0] += 1
        else:
            obj.img_list[21] = ''
        if 'touchpad' in obj.parameters:
            price += db_handler.plc_price((6, ), obj.data_base)
            spec.append(db_handler.plc_obj((6, ), obj.data_base))
    elif obj.system_type == 'Out':
        if "switch_type" in obj.parameters:
            obj.img_list[13] = img_data.cabinet_img['33']
            sign[0] += 1
        else:
            obj.img_list[13] = img_data.cabinet_img['32']
            sign[0] += 1
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[9] = img_data.cabinet_img['27']
            sign[0] += 1
        else:
            obj.img_list[9] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            if obj.numer_param['disp_protocol'] == '1':
                if obj.numer_param['sensor_temp_outdoor_type'] == 'chanel':
                    obj.img_list[1] = img_data.cabinet_img['28']
                    obj.img_list[0] = img_data.cabinet_img['23']
                    price += db_handler.sensors_price((3,), obj.data_base)
                    spec.append(db_handler.sensors_obj((3,), obj.data_base))
                elif obj.numer_param['sensor_temp_outdoor_type'] == 'outdoor':
                    obj.img_list[0] = img_data.cabinet_img['24']
                    obj.img_list[1] = ''
                    price += db_handler.sensors_price((1,), obj.data_base)
                    spec.append(db_handler.sensors_obj((1,), obj.data_base))
            elif obj.numer_param['disp_protocol'] == '2':
                if obj.numer_param['sensor_temp_outdoor_type'] == 'chanel':
                    obj.img_list[1] = img_data.cabinet_img['28']
                    obj.img_list[0] = img_data.cabinet_img['37']
                    price += db_handler.sensors_price((3,), obj.data_base)
                    spec.append(db_handler.sensors_obj((3,), obj.data_base))
                elif obj.numer_param['sensor_temp_outdoor_type'] == 'outdoor':
                    obj.img_list[0] = img_data.cabinet_img['36']
                    obj.img_list[1] = ''
                    price += db_handler.sensors_price((1,), obj.data_base)
                    spec.append(db_handler.sensors_obj((1,), obj.data_base))
            sign[2] += 1
        else:
            if 'disp_protocol' in obj.numer_param and obj.numer_param['disp_protocol'] == '2':
                obj.img_list[0] = img_data.cabinet_img['37']
                obj.img_list[1] = ''
            else:
                obj.img_list[0] = img_data.cabinet_img['23']
                obj.img_list[1] = ''
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[15] = img_data.cabinet_img['26']
            sign[2] += 1
            price += db_handler.sensors_price((9,), obj.data_base)
            spec.append(db_handler.sensors_obj((9,), obj.data_base))
        else:
            obj.img_list[15] = img_data.cabinet_img['25']
        if 'sensor_hood_out' in obj.parameters:
            obj.img_list[14] = img_data.cabinet_img['28']
            sign[2] += 1
            price += db_handler.sensors_price((3,), obj.data_base)
            spec.append(db_handler.sensors_obj((3,), obj.data_base))
        else:
            obj.img_list[14] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[10] = img_data.cabinet_img['29']
            sign[4] += 1
        else:
            obj.img_list[10] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[11] = img_data.cabinet_img['30']
            sign[4] += 1
        else:
            obj.img_list[11] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[12] = img_data.cabinet_img['31']
            sign[0] += 1
        else:
            obj.img_list[12] = ''
        if 'touchpad' in obj.parameters:
            price += db_handler.plc_price((6, ), obj.data_base)
            spec.append(db_handler.plc_obj((6, ), obj.data_base))
    return [price, sign, spec]


def vent_power_in(obj):
    price = 0
    sign = [0, 0, 0, 0, 0]
    spec = []
    if obj.system_type != "Out":
        if 'voltage_vent_in' in obj.numer_param and obj.numer_param['voltage_vent_in'] == '380':
            start_id = 13
            br_id = start_id + int(obj.numer_param['vent_power_in'])
        else:
            start_id = 3
            br_id = start_id + int(obj.numer_param['vent_power_in'])
            if br_id > 10:
                br_id = 10
        quantity = 1
        reserv = 0
        if 'vent_quant_in' in obj.numer_param:
            quantity = int(obj.numer_param['vent_quant_in'])
        if 'reserv_in' in obj.numer_param:
            if obj.numer_param['reserv_in'] == 'no_reserv':
                reserv = 0
            else:
                reserv = 1
        breaker = db_handler.breaker_price((br_id,), obj.data_base) * (quantity + reserv)
        for i in range(quantity+reserv):
            spec.append(db_handler.breaker_obj((br_id,), obj.data_base))
            breaker += db_handler.breaker_price((1,), obj.data_base)
            spec.append(db_handler.breaker_obj((1,), obj.data_base))
        if 'FC_in' in obj.numer_param:
            if obj.numer_param["FC_in"] == "FC":
                power_price = db_handler.fc_price((int(obj.numer_param['vent_power_in']) + 1, ), obj.data_base) * (quantity + reserv)
                for i in range(quantity+reserv):
                    spec.append(db_handler.fc_obj((int(obj.numer_param['vent_power_in']) + 1,), obj.data_base))
                sign[0] += quantity+reserv
                sign[4] += quantity+reserv
                if 'smooth_in' in obj.parameters:
                    sign[3] += 1 * (quantity+reserv)
                    if 'pressure_maint_in' in obj.parameters:
                        sign[2] += 1
                        power_price += db_handler.sensors_price((10,), obj.data_base)
                        spec.append(db_handler.sensors_obj((10,), obj.data_base))
            elif obj.numer_param["FC_in"] == "NOT_FC":
                sign[0] += quantity + reserv
                sign[4] += quantity + reserv
                cont_id = 1
                if int(obj.numer_param['vent_power_in']) > 4:
                    cont_id = int(obj.numer_param['vent_power_in']) - 3
                power_price = db_handler.contactor_price((cont_id, ), obj.data_base) * (quantity + reserv)
                for i in range(quantity+reserv):
                    spec.append(db_handler.contactor_obj((cont_id,), obj.data_base))
            elif obj.numer_param["FC_in"] == "EC":
                power_price = 0
                sign[0] += quantity + reserv
                sign[3] += 1 * (quantity+reserv)
                if 'pressure_maint_in' in obj.parameters:
                    sign[2] += 1
                    power_price += db_handler.sensors_price((10,), obj.data_base)
                    spec.append(db_handler.sensors_obj((10,), obj.data_base))
            elif obj.numer_param["FC_in"] == "potentiometr":
                sign[4] += quantity + reserv
                power_price = db_handler.mont_elements_price((12,), obj.data_base) * (
                            quantity + reserv)
                for i in range(quantity + reserv):
                    spec.append(db_handler.mont_elements_obj((12,), obj.data_base))
        if 'dif_in' in obj.parameters:
            res_dif = 0
            if 'reserv_in' in obj.numer_param:
                if obj.numer_param['reserv_in'] == 'vent_reserv_in' and obj.numer_param['quant_dif_in'] == '2':
                    res_dif = 1
            dif = db_handler.diff_price(obj.data_base) * quantity+res_dif
            dif += db_handler.relay_price(obj.data_base) * quantity+res_dif
            for i in range(quantity+res_dif):
                spec.append(db_handler.diff_obj(obj.data_base))
                for j in db_handler.relay_obj(obj.data_base):
                    spec.append(j)
                sign[0] += 1
        else:
            dif = 0
        if 'reserv_in' in obj.numer_param:
            if obj.numer_param['reserv_in'] == 'vent_reserv_in':
                damp_quantity = int(obj.numer_param['damp_vent_quant_in'])
                if int(obj.numer_param['vent_damp_type_in']) < 9:
                    power_price += db_handler.relay_price(obj.data_base)*damp_quantity
                    for i in range(damp_quantity):
                        for j in db_handler.relay_obj(obj.data_base):
                            spec.append(j)
                    sign[4] += damp_quantity
                else:
                    sign[3] += damp_quantity
                power_price += db_handler.drive_price((int(obj.numer_param['vent_damp_type_in']) + 1,), obj.data_base)*damp_quantity
                for i in range(damp_quantity):
                    spec.append(db_handler.drive_obj((int(obj.numer_param['vent_damp_type_in']) + 1,), obj.data_base))
                if 'vent_damp_confirm_in' in obj.parameters:
                    if int(obj.numer_param['vent_damp_type_in']) < 9:
                        sign[0] += damp_quantity
                    else:
                        sign[2] += damp_quantity
                if 'vent_damp_heat_in' in obj.parameters:
                    sign[4] += damp_quantity
                    if 'vent_damp_heat_voltage_in' in obj.parameters:
                        vent_heat_br_id = 15
                    else:
                        vent_heat_br_id = 4
                    power_price += db_handler.breaker_price((vent_heat_br_id,), obj.data_base)*damp_quantity
                    power_price += db_handler.contactor_price((1,), obj.data_base)*damp_quantity
                    for i in range(damp_quantity):
                        spec.append(db_handler.breaker_obj((vent_heat_br_id,), obj.data_base))
                        spec.append(db_handler.contactor_obj((1,), obj.data_base))
        relay = 2 * db_handler.relay_price(obj.data_base) * (quantity+reserv)
        for i in range((quantity+reserv)*2):
            for j in db_handler.relay_obj(obj.data_base):
                spec.append(j)
        if 'vent_termo_protect_in' in obj.numer_param:
            if obj.numer_param['vent_termo_protect_in'] == 'thermo':
                sign[0] += quantity+reserv
            elif obj.numer_param['vent_termo_protect_in'] == 'thermistor':
                sign[0] += quantity + reserv
                power_price += db_handler.mont_elements_price((11,), obj.data_base) * (quantity + reserv)
                for i in range((quantity + reserv)):
                    spec.append(db_handler.mont_elements_obj((11,), obj.data_base))
        price = power_price + dif + breaker + relay
    return [price, sign, spec]


def vent_power_out(obj):
    price = 0
    sign = [0, 0, 0, 0, 0]
    spec = []
    if obj.system_type != "In":
        if 'voltage_vent_out' in obj.numer_param and obj.numer_param['voltage_vent_out'] == '380':
            start_id = 13
            br_id = start_id + int(obj.numer_param['vent_power_out'])
        else:
            start_id = 3
            br_id = start_id + int(obj.numer_param['vent_power_out'])
            if br_id > 10:
                br_id = 10
        quantity = 1
        reserv = 0
        if 'vent_quant_out' in obj.numer_param:
            quantity = int(obj.numer_param['vent_quant_out'])
        if 'reserv_out' in obj.numer_param:
            if obj.numer_param['reserv_out'] == 'no_reserv':
                reserv = 0
            else:
                reserv = 1
        breaker = db_handler.breaker_price((br_id,), obj.data_base) * (quantity + reserv)
        for i in range(quantity+reserv):
            spec.append(db_handler.breaker_obj((br_id,), obj.data_base))
            breaker += db_handler.breaker_price((1,), obj.data_base)
            spec.append(db_handler.breaker_obj((1,), obj.data_base))
        if 'FC_out' in obj.numer_param:
            if obj.numer_param["FC_out"] == "FC":
                power_price = db_handler.fc_price((int(obj.numer_param['vent_power_out']) + 1, ), obj.data_base) * (quantity + reserv)
                for i in range(quantity+reserv):
                    spec.append(db_handler.fc_obj((int(obj.numer_param['vent_power_out']) + 1,), obj.data_base))
                sign[0] += quantity+reserv
                sign[4] += quantity+reserv
                if 'smooth_out' in obj.parameters:
                    sign[3] += 1 * (quantity+reserv)
                    if 'pressure_maint_out' in obj.parameters:
                        sign[2] += 1
                        power_price += db_handler.sensors_price((10,), obj.data_base)
                        spec.append(db_handler.sensors_obj((10,), obj.data_base))
            elif obj.numer_param["FC_out"] == "NOT_FC":
                sign[0] += quantity + reserv
                sign[4] += quantity + reserv
                cont_id = 1
                if int(obj.numer_param['vent_power_out']) > 4:
                    cont_id = int(obj.numer_param['vent_power_out']) - 3
                power_price = db_handler.contactor_price((cont_id, ), obj.data_base) * (quantity + reserv)
                for i in range(quantity+reserv):
                    spec.append(db_handler.contactor_obj((cont_id,), obj.data_base))
            elif obj.numer_param["FC_out"] == "EC":
                power_price = 0
                sign[0] += quantity + reserv
                sign[3] += 1 * (quantity+reserv)
                if 'pressure_maint_out' in obj.parameters:
                    sign[2] += 1
                    power_price += db_handler.sensors_price((10,), obj.data_base)
                    spec.append(db_handler.sensors_obj((10,), obj.data_base))
            elif obj.numer_param["FC_out"] == "potentiometr":
                sign[4] += quantity + reserv
                power_price = db_handler.mont_elements_price((12,), obj.data_base) * (
                        quantity + reserv)
                for i in range(quantity + reserv):
                    spec.append(db_handler.mont_elements_obj((12,), obj.data_base))
        if 'dif_out' in obj.parameters:
            res_dif = 0
            if 'reserv_out' in obj.numer_param:
                if obj.numer_param['reserv_out'] == 'vent_reserv_out' and obj.numer_param['quant_dif_out'] == '2':
                    res_dif = 1
            dif = db_handler.diff_price(obj.data_base) * quantity+res_dif
            dif += db_handler.relay_price(obj.data_base) * quantity+res_dif
            for i in range(quantity+res_dif):
                spec.append(db_handler.diff_obj(obj.data_base))
                for j in db_handler.relay_obj(obj.data_base):
                    spec.append(j)
                sign[0] += 1
        else:
            dif = 0
        if 'reserv_out' in obj.numer_param:
            if obj.numer_param['reserv_out'] == 'vent_reserv_out':
                damp_quantity = int(obj.numer_param['damp_vent_quant_out'])
                if int(obj.numer_param['vent_damp_type_out']) < 9:
                    power_price += db_handler.relay_price(obj.data_base)*damp_quantity
                    for i in range(damp_quantity):
                        for j in db_handler.relay_obj(obj.data_base):
                            spec.append(j)
                    sign[4] += damp_quantity
                else:
                    sign[3] += damp_quantity
                power_price += db_handler.drive_price((int(obj.numer_param['vent_damp_type_out']) + 1,), obj.data_base)*damp_quantity
                for i in range(damp_quantity):
                    spec.append(db_handler.drive_obj((int(obj.numer_param['vent_damp_type_out']) + 1,), obj.data_base))
                if 'vent_damp_confirm_out' in obj.parameters:
                    if int(obj.numer_param['vent_damp_type_out']) < 9:
                        sign[0] += damp_quantity
                    else:
                        sign[2] += damp_quantity
                if 'vent_damp_heat_out' in obj.parameters:
                    sign[4] += damp_quantity
                    if 'vent_damp_heat_voltage_out' in obj.parameters:
                        vent_heat_br_id = 15
                    else:
                        vent_heat_br_id = 4
                    power_price += db_handler.breaker_price((vent_heat_br_id,), obj.data_base)*damp_quantity
                    power_price += db_handler.contactor_price((1,), obj.data_base)*damp_quantity
                    for i in range(damp_quantity):
                        spec.append(db_handler.breaker_obj((vent_heat_br_id,), obj.data_base))
                        spec.append(db_handler.contactor_obj((1,), obj.data_base))
        relay = 2 * db_handler.relay_price(obj.data_base) * (quantity+reserv)
        for i in range((quantity+reserv)*2):
            for j in db_handler.relay_obj(obj.data_base):
                spec.append(j)
        if 'vent_termo_protect_out' in obj.numer_param:
            if obj.numer_param['vent_termo_protect_out'] == 'thermo':
                sign[0] += quantity+reserv
            elif obj.numer_param['vent_termo_protect_out'] == 'thermistor':
                sign[0] += quantity + reserv
                power_price += db_handler.mont_elements_price((11,), obj.data_base) * (quantity+reserv)
                for i in range((quantity+reserv)):
                    spec.append(db_handler.mont_elements_obj((11,), obj.data_base))
        price = power_price + dif + breaker + relay
    return [price, sign, spec]


def type_handling(system_type):
    if system_type == "In_out":
        return {"FC_in": "FC", "FC_out": "FC", "vent_power_in": '0', "vent_power_out": '0',
                'shutdown_fire_signal': 'true', 'signal_work': 'true', 'signal_alarm': 'true'}
    elif system_type == "In":
        return {"FC_in": "FC", "vent_power_in": '0', 'shutdown_fire_signal': 'true', 'signal_work': 'true',
                'signal_alarm': 'true'}
    elif system_type == "Out":
        return {'FC_out': 'FC', "vent_power_out": '0', 'shutdown_fire_signal': 'true', 'signal_work': 'true',
                'signal_alarm': 'true'}


def get_panel(obj):
    index = 1
    fc_const = 2
    quantity_in = 1
    quantity_out = 1
    if 'vent_quant_in' in obj.numer_param or 'vent_quant_out' in obj.numer_param:
        quantity_in = int(obj.numer_param['vent_quant_in']) + 1
        quantity_out = int(obj.numer_param['vent_quant_out']) + 1
    contactor_const = 1
    power_metric = 0
    if obj.system_type == "In_out":
        if obj.numer_param["FC_in"] == "FC" and obj.numer_param["FC_out"] == "FC":
            power_metric = int(obj.numer_param['vent_power_in']) * fc_const * quantity_in + int(obj.numer_param[
                'vent_power_out']) * fc_const * quantity_out
        elif obj.numer_param["FC_in"] == "FC" and obj.numer_param["FC_out"] != "FC":
            power_metric = int(obj.numer_param['vent_power_in']) * fc_const * quantity_in + int(obj.numer_param[
                'vent_power_out']) * contactor_const * quantity_out
        elif obj.numer_param["FC_in"] != "FC" and obj.numer_param["FC_out"] == "FC":
            power_metric = int(obj.numer_param['vent_power_in']) * contactor_const * quantity_in + int(obj.numer_param[
                'vent_power_out']) * fc_const * quantity_out
        else:
            power_metric = int(obj.numer_param['vent_power_in']) * contactor_const * quantity_in + int(obj.numer_param[
                'vent_power_out']) * contactor_const * quantity_out
    elif obj.system_type == "In":
        if obj.numer_param["FC_in"] == "FC":
            power_metric = (int(obj.numer_param['vent_power_in']) * fc_const + 8) * quantity_in
        else:
            power_metric = int(obj.numer_param['vent_power_in']) * contactor_const * quantity_in
    elif obj.system_type == "Out":
        if obj.numer_param["FC_out"] == "FC":
            power_metric = (int(obj.numer_param['vent_power_out']) * fc_const + 8) * quantity_out
        else:
            power_metric = int(obj.numer_param['vent_power_out']) * contactor_const * quantity_out
    if power_metric >= 52:
        index += 5
    elif 52 > power_metric >= 40:
        index += 4
    elif 40 > power_metric >= 28:
        index += 3
    elif 28 > power_metric >= 20:
        index += 2
    elif 20 > power_metric >= 12:
        index += 1
    panel_obj = db_handler.panel_obj((index, ), obj.data_base)
    panel_price = db_handler.panel_price((index, ), obj.data_base)
    return panel_price, [0, 0, 0, 0, 0], [panel_obj]


def add_static_elements(obj):
    data = db_handler.get_static_el(obj.data_base)
    data[0].insert(5, 300)
    data[1].insert(5, 100)
    data[2].insert(5, 100)
    data[3].insert(5, 100)
    data[4].insert(5, 1)
    data[5].insert(5, 2)
    data[6].insert(5, 2)
    data[7].insert(5, 2)
    data[8].insert(5, 1)
    data[9].insert(5, 1)
    data[10].insert(5, 1)
    data[11].insert(5, 2)
    data[12].insert(5, 1)

    for i, j in enumerate(data):
        summa = float(j[-1]) * j[-3]
        obj.price += summa
        data[i].append(summa)
    obj.static_elements = data





