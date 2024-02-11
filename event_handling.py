import img_data
import db_handler


def vent_in(system_type, parameters, num_param, img_list):
    if 'dif_in' in parameters:
        if 'FC_in' in parameters:
            if system_type == 'In_out':
                key = '3'
            elif system_type == "In":
                key = '7'
        else:
            if system_type == 'In_out':
                key = '1'
            elif system_type == "In":
                key = '5'
    else:
        if 'FC_in' in parameters:
            if system_type == 'In_out':
                key = '2'
            elif system_type == "In":
                key = '6'
        else:
            if system_type == 'In_out':
                key = '0'
            elif system_type == "In":
                key = '4'
    img_list[8] = img_data.vent_in_img[key]
    return 0


def vent_out(system_type, parameters, num_param, img_list):
    index = 9 if system_type == 'In_out' else 7
    if 'dif_out' in parameters:
        if 'FC_out' in parameters:
            if system_type == 'In_out':
                key = '3'
            elif system_type == "Out":
                key = '7'
        else:
            if system_type == 'In_out':
                key = '1'
            elif system_type == "Out":
                key = '5'
    else:
        if 'FC_out' in parameters:
            if system_type == 'In_out':
                key = '2'
            elif system_type == "Out":
                key = '6'
        else:
            if system_type == 'In_out':
                key = '0'
            elif system_type == "Out":
                key = '4'
    img_list[index] = img_data.vent_out_img[key]
    return 0


def first_heater(system_type, parameters, num_param, img_list):
    if 'select_0' not in parameters:
        for i in range(0, 4):
            img_list[i+4] = ''
    if system_type == "In_out":
        if 'first_heater_type' not in parameters:
            if 'select_0' in parameters and 'first_confirm' in parameters:
                key = '0'
            elif 'select_0' in parameters and 'first_confirm' not in parameters:
                key = '1'
            if 'first_thermostat' in parameters:
                img_list[5] = img_data.heater_img['10']
            else:
                img_list[5] = ''
        elif 'first_heater_type' in parameters:
            img_list[5] = ''
            if 'select_0' in parameters and 'first_electrical_thermal' in num_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[num_param['first_electrical_thermal']]
    elif system_type == 'In':
        if 'first_heater_type' not in parameters:
            if 'select_0' in parameters and 'first_confirm' in parameters:
                key = '5'
            elif 'select_0' in parameters and 'first_confirm' not in parameters:
                key = '6'
            if 'first_thermostat' in parameters:
                img_list[5] = img_data.heater_img['11']
            else:
                img_list[5] = ''
        elif 'first_heater_type' in parameters:
            img_list[5] = ''
            if 'select_0' in parameters and 'first_electrical_thermal' in num_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[num_param['first_electrical_thermal']]
    img_list[4] = img_data.heater_img[key]
    return 1000


def second_heater(system_type, parameters, num_param, img_list):
    if system_type == "In_out":
        if 'second_heat_choice' in parameters and 'second_heat_type' not in parameters:
            if 'select_0' in parameters and 'second_confirm' in parameters and 'second_sensor' in parameters:
                key = '0'
            elif 'select_0' in parameters and 'second_confirm' not in parameters and 'second_sensor' in parameters:
                key = '1'
            elif 'select_0' in parameters and 'second_confirm' not in parameters and 'second_sensor' not in parameters:
                key = '14'
            elif 'select_0' in parameters and 'second_confirm' in parameters and 'second_sensor' not in parameters:
                key = '15'
            if 'second_thermostat' in parameters:
                img_list[7] = img_data.heater_img['10']
            else:
                img_list[7] = ''
        elif 'second_heat_choice' in parameters and 'second_heat_type' in parameters:
            img_list[7] = ''
            if 'select_0' in parameters and 'second_electrical_thermal' in num_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[num_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in parameters:
            key = '16'
            img_list[7] = ''
    elif system_type == 'In':
        if 'second_heat_choice' in parameters and 'second_heat_type' not in parameters:
            if 'select_0' in parameters and 'second_confirm' in parameters and 'second_sensor' in parameters:
                key = '5'
            elif 'select_0' in parameters and 'second_confirm' not in parameters and 'second_sensor' in parameters:
                key = '6'
            elif 'select_0' in parameters and 'second_confirm' not in parameters and 'second_sensor' not in parameters:
                key = '12'
            elif 'select_0' in parameters and 'second_confirm' in parameters and 'second_sensor' not in parameters:
                key = '13'
            if 'second_thermostat' in parameters:
                img_list[7] = img_data.heater_img['11']
            else:
                img_list[7] = ''
        elif 'second_heat_choice' in parameters and 'second_heat_type' in parameters:
            img_list[7] = ''
            if 'select_0' in parameters and 'second_electrical_thermal' in num_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[num_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in parameters:
            key = '16'
            img_list[7] = ''
    img_list[6] = img_data.heater_img[key]
    return 1000


def dampers(system_type, parameters, num_param, img_list):
    if system_type == "In_out":
        if 'damp_in' in parameters:
            if 'in_damper_confirm' in parameters and 'in_damper_heat' in parameters:
                key_in = '0'
            elif 'in_damper_confirm' in parameters and 'in_damper_heat' not in parameters:
                key_in = '1'
            elif 'in_damper_confirm' not in parameters and 'in_damper_heat' in parameters:
                key_in = '2'
            elif 'in_damper_confirm' not in parameters and 'in_damper_heat' not in parameters:
                key_in = '3'
            img_list[1] = img_data.dampers_img[key_in]
        else:
            img_list[1] = ''
        if 'damp_out' in parameters:
            if 'out_damper_confirm' in parameters and 'out_damper_heat' in parameters:
                key_out = '4'
            elif 'out_damper_confirm' in parameters and 'out_damper_heat' not in parameters:
                key_out = '5'
            elif 'out_damper_confirm' not in parameters and 'out_damper_heat' in parameters:
                key_out = '6'
            elif 'out_damper_confirm' not in parameters and 'out_damper_heat' not in parameters:
                key_out = '7'
            img_list[2] = img_data.dampers_img[key_out]
        else:
            img_list[2] = ''
    elif system_type == 'In':
        img_list[2] = ''
        if 'damp_in' in parameters:
            if 'in_damper_confirm' in parameters and 'in_damper_heat' in parameters:
                key_in = '8'
            elif 'in_damper_confirm' in parameters and 'in_damper_heat' not in parameters:
                key_in = '9'
            elif 'in_damper_confirm' not in parameters and 'in_damper_heat' in parameters:
                key_in = '10'
            elif 'in_damper_confirm' not in parameters and 'in_damper_heat' not in parameters:
                key_in = '11'
            img_list[1] = img_data.dampers_img[key_in]
        else:
            img_list[1] = ''
    return 1000


def filters(system_type, parameters, num_param, img_list, specification):
    if system_type == 'In_out':
        if 'filt_in' in parameters:
            if 'in_filter_quantity' in num_param:
                variant = [3, 11, 12]
                for i in variant[:int(num_param['in_filter_quantity'])+1]:
                    img_list[i] = img_data.filters_img['0']
                for i in variant[int(num_param['in_filter_quantity'])+1:]:
                    img_list[i] = ''
        elif "filt_in" not in parameters:
            img_list[3], img_list[11], img_list[12] = '', '', ''
        if 'filt_out' in parameters:
            img_list[10] = img_data.filters_img['1']
        elif 'filt_out' not in parameters:
            img_list[10] = ''
    elif system_type == 'In':
        if 'filt_in' in parameters:
            if 'in_filter_quantity' in num_param:
                variant = [3, 9, 10]
                for i in variant[:int(num_param['in_filter_quantity'])+1]:
                    img_list[i] = img_data.filters_img['2']
                for i in variant[int(num_param['in_filter_quantity'])+1:]:
                    img_list[i] = ''
        elif "filt_in" not in parameters:
            img_list[3], img_list[9], img_list[10] = '', '', ''
    if 'filt_in' in parameters or 'filt_out' in parameters:
        return 1000
    return 0


def cabinet (system_type, parameters, num_param, img_list):
    if system_type == "In_out":
        if "switch_type" in parameters:
            img_list[17] = img_data.cabinet_img['1']
        else:
            img_list[17] = img_data.cabinet_img['0']
        if 'shutdown_fire_signal' in parameters:
            img_list[13] = img_data.cabinet_img['2']
        else:
            img_list[13] = ''
        if 'sensor_temp_outdoor' in parameters:
            img_list[0] = img_data.cabinet_img['4']
        else:
            img_list[0] = img_data.cabinet_img['3']
        if 'sensor_temp_indoor' in parameters:
            img_list[20] = img_data.cabinet_img['6']
        else:
            img_list[20] = img_data.cabinet_img['5']
        if 'sensor_humid' in parameters:
            img_list[18] = img_data.cabinet_img['7']
        else:
            img_list[18] = ''
        if 'sensor_hood' in parameters:
            img_list[19] = img_data.cabinet_img['8']
        else:
            img_list[19] = ''
        if 'signal_work' in parameters:
            img_list[14] = img_data.cabinet_img['9']
        else:
            img_list[14] = ''
        if 'signal_alarm' in parameters:
            img_list[15] = img_data.cabinet_img['10']
        else:
            img_list[15] = ''
        if 'remote_control' in parameters:
            img_list[16] = img_data.cabinet_img['11']
        else:
            img_list[16] = ''
    elif system_type == 'In':
        if "switch_type" in parameters:
            img_list[15] = img_data.cabinet_img['13']
        else:
            img_list[15] = img_data.cabinet_img['12']
        if 'shutdown_fire_signal' in parameters:
            img_list[11] = img_data.cabinet_img['14']
        else:
            img_list[11] = ''
        if 'sensor_temp_outdoor' in parameters:
            img_list[0] = img_data.cabinet_img['16']
        else:
            img_list[0] = img_data.cabinet_img['15']
        if 'sensor_temp_indoor' in parameters:
            img_list[17] = img_data.cabinet_img['17']
        else:
            img_list[17] = img_data.cabinet_img['18']
        if 'sensor_humid' in parameters:
            img_list[16] = img_data.cabinet_img['19']
        else:
            img_list[16] = ''
        if 'signal_work' in parameters:
            img_list[12] = img_data.cabinet_img['20']
        else:
            img_list[12] = ''
        if 'signal_alarm' in parameters:
            img_list[13] = img_data.cabinet_img['21']
        else:
            img_list[13] = ''
        if 'remote_control' in parameters:
            img_list[14] = img_data.cabinet_img['22']
        else:
            img_list[14] = ''
    return 1000


def vent_power_in(system_type, parameters, num_param, img_list, specification):
    if int(num_param['vent_power_in']) <= 5:
        br_id = 3
    elif 5 < int(num_param['vent_power_in']) < 9:
        br_id = 2
    elif int(num_param['vent_power_in']) >= 9:
        br_id = 1
    breaker = db_handler.breaker_price((br_id,))
    specification.append(db_handler.breaker_obj((br_id,)))
    breaker += 2 * db_handler.breaker_price((5,))
    specification.append(db_handler.breaker_obj((5,)))
    if 'FC_in' in parameters:
        power_price = db_handler.fc_price((int(num_param['vent_power_in']) + 1, ))
        specification.append(db_handler.fc_obj((int(num_param['vent_power_in']) + 1,)))
    else:
        if int(num_param['vent_power_in']) <= 8:
            cont_id = 1
        elif 8 < int(num_param['vent_power_in']) <= 14:
            cont_id = int(num_param['vent_power_in']) - 7
        else:
            cont_id = 7
        power_price = db_handler.contactor_price((cont_id, ))
        specification.append(db_handler.contactor_obj((cont_id,)))
    if 'dif_in' in parameters:
        dif = db_handler.diff_price()
        specification.append(db_handler.diff_obj())
    else:
        dif = 0
    relay = 2 * db_handler.relay_price()
    for i in db_handler.relay_obj():
        specification.append(list(i))
    for i in db_handler.relay_obj():
        specification.append(list(i))
    # plc = db_handler.plc_price((3,))
    return power_price + dif + breaker + relay


def vent_power_out(system_type, parameters, num_param, img_list, specification):
    if int(num_param['vent_power_out']) <= 5:
        br_id = 3
    elif 5 < int(num_param['vent_power_out']) < 9:
        br_id = 2
    elif int(num_param['vent_power_out']) >= 9:
        br_id = 1
    breaker = db_handler.breaker_price((br_id,))
    specification.append(db_handler.breaker_obj((br_id, )))
    breaker += 2 * db_handler.breaker_price((5,))
    specification.append(db_handler.breaker_obj((5,)))
    if 'FC_out' in parameters:
        power_price = db_handler.fc_price((int(num_param['vent_power_out']) + 1, ))
        specification.append(db_handler.fc_obj((int(num_param['vent_power_out']) + 1, )))
    else:
        if int(num_param['vent_power_out']) <= 8:
            cont_id = 1
        elif 8 < int(num_param['vent_power_out']) <= 14:
            cont_id = int(num_param['vent_power_out']) - 7
        else:
            cont_id = 7
        power_price = db_handler.contactor_price((cont_id, ))
        specification.append(db_handler.contactor_obj((cont_id,)))
    if 'dif_out' in parameters:
        dif = db_handler.diff_price()
        specification.append(db_handler.diff_obj())
    else:
        dif = 0
    relay = 2 * db_handler.relay_price()
    for i in db_handler.relay_obj():
        specification.append(list(i))
    for i in db_handler.relay_obj():
        specification.append(list(i))
    return power_price + dif + breaker + relay


def type_handling(system_type):
    if system_type == "In_out":
        return {"FC_in": "true", "FC_out": "true", "vent_power_in": '0', "vent_power_out": '0'}
    elif system_type == "In":
        return {"FC_in": "true", "vent_power_in": '0'}
    elif system_type == "Out":
        return {'FC_out': 'true', "vent_power_out": '0'}


