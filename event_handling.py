import img_data
import db_handler


def vent_in(obj):
    if 'dif_in' in obj.parameters:
        if 'FC_in' in obj.parameters:
            if obj.system_type == 'In_out':
                key = '3'
            elif obj.system_type == "In":
                key = '7'
        else:
            if obj.system_type == 'In_out':
                key = '1'
            elif obj.system_type == "In":
                key = '5'
    else:
        if 'FC_in' in obj.parameters:
            if obj.system_type == 'In_out':
                key = '2'
            elif obj.system_type == "In":
                key = '6'
        else:
            if obj.system_type == 'In_out':
                key = '0'
            elif obj.system_type == "In":
                key = '4'
    obj.img_list[8] = img_data.vent_in_img[key]
    return 0


def vent_out(obj):
    index = 9 if obj.system_type == 'In_out' else 7
    if 'dif_out' in obj.parameters:
        if 'FC_out' in obj.parameters:
            if obj.system_type == 'In_out':
                key = '3'
            elif obj.system_type == "Out":
                key = '7'
        else:
            if obj.system_type == 'In_out':
                key = '1'
            elif obj.system_type == "Out":
                key = '5'
    else:
        if 'FC_out' in obj.parameters:
            if obj.system_type == 'In_out':
                key = '2'
            elif obj.system_type == "Out":
                key = '6'
        else:
            if obj.system_type == 'In_out':
                key = '0'
            elif obj.system_type == "Out":
                key = '4'
    obj.img_list[index] = img_data.vent_out_img[key]
    return 0


def first_heater(obj):
    if 'select_0' not in obj.parameters:
        for i in range(0, 4):
            obj.img_list[i+4] = ''
    if obj.system_type == "In_out":
        if 'first_heater_type' not in obj.parameters:
            if 'select_0' in obj.parameters and 'first_confirm' in obj.parameters:
                key = '0'
            elif 'select_0' in obj.parameters and 'first_confirm' not in obj.parameters:
                key = '1'
            if 'first_thermostat' in obj.parameters:
                obj.img_list[5] = img_data.heater_img['10']
            else:
                obj.img_list[5] = ''
        elif 'first_heater_type' in obj.parameters:
            obj.img_list[5] = ''
            if 'select_0' in obj.parameters and 'first_electrical_thermal' in obj.numer_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[obj.numer_param['first_electrical_thermal']]
    elif obj.system_type == 'In':
        if 'first_heater_type' not in obj.parameters:
            if 'select_0' in obj.parameters and 'first_confirm' in obj.parameters:
                key = '5'
            elif 'select_0' in obj.parameters and 'first_confirm' not in obj.parameters:
                key = '6'
            if 'first_thermostat' in obj.parameters:
                obj.img_list[5] = img_data.heater_img['11']
            else:
                obj.img_list[5] = ''
        elif 'first_heater_type' in obj.parameters:
            obj.img_list[5] = ''
            if 'select_0' in obj.parameters and 'first_electrical_thermal' in obj.numer_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[obj.numer_param['first_electrical_thermal']]
    obj.img_list[4] = img_data.heater_img[key]
    return 1000


def second_heater(obj):
    if obj.system_type == "In_out":
        if 'second_heat_choice' in obj.parameters and 'second_heat_type' not in obj.parameters:
            if 'select_0' in obj.parameters and 'second_confirm' in obj.parameters and 'second_sensor' in obj.parameters:
                key = '0'
            elif 'select_0' in obj.parameters and 'second_confirm' not in obj.parameters and 'second_sensor' in obj.parameters:
                key = '1'
            elif 'select_0' in obj.parameters and 'second_confirm' not in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '14'
            elif 'select_0' in obj.parameters and 'second_confirm' in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '15'
            if 'second_thermostat' in obj.parameters:
                obj.img_list[7] = img_data.heater_img['10']
            else:
                obj.img_list[7] = ''
        elif 'second_heat_choice' in obj.parameters and 'second_heat_type' in obj.parameters:
            obj.img_list[7] = ''
            if 'select_0' in obj.parameters and 'second_electrical_thermal' in obj.numer_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[obj.obj.numer_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in obj.parameters:
            key = '16'
            obj.img_list[7] = ''
    elif obj.system_type == 'In':
        if 'second_heat_choice' in obj.parameters and 'second_heat_type' not in obj.parameters:
            if 'select_0' in obj.parameters and 'second_confirm' in obj.parameters and 'second_sensor' in obj.parameters:
                key = '5'
            elif 'select_0' in obj.parameters and 'second_confirm' not in obj.parameters and 'second_sensor' in obj.parameters:
                key = '6'
            elif 'select_0' in obj.parameters and 'second_confirm' not in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '12'
            elif 'select_0' in obj.parameters and 'second_confirm' in obj.parameters and 'second_sensor' not in obj.parameters:
                key = '13'
            if 'second_thermostat' in obj.parameters:
                obj.img_list[7] = img_data.heater_img['11']
            else:
                obj.img_list[7] = ''
        elif 'second_heat_choice' in obj.parameters and 'second_heat_type' in obj.parameters:
            obj.img_list[7] = ''
            if 'select_0' in obj.parameters and 'second_electrical_thermal' in obj.obj.numer_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[obj.numer_param['second_electrical_thermal']]
        elif 'second_heat_choice' not in obj.parameters:
            key = '16'
            obj.img_list[7] = ''
    obj.img_list[6] = img_data.heater_img[key]
    return 1000


def dampers(obj):
    if obj.system_type == "In_out":
        if 'damp_in' in obj.parameters:
            if 'in_damper_confirm' in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '0'
            elif 'in_damper_confirm' in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '1'
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '2'
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '3'
            obj.img_list[1] = img_data.dampers_img[key_in]
        else:
            obj.img_list[1] = ''
        if 'damp_out' in obj.parameters:
            if 'out_damper_confirm' in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '4'
            elif 'out_damper_confirm' in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '5'
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' in obj.parameters:
                key_out = '6'
            elif 'out_damper_confirm' not in obj.parameters and 'out_damper_heat' not in obj.parameters:
                key_out = '7'
            obj.img_list[2] = img_data.dampers_img[key_out]
        else:
            obj.img_list[2] = ''
    elif obj.system_type == 'In':
        obj.img_list[2] = ''
        if 'damp_in' in obj.parameters:
            if 'in_damper_confirm' in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '8'
            elif 'in_damper_confirm' in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '9'
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' in obj.parameters:
                key_in = '10'
            elif 'in_damper_confirm' not in obj.parameters and 'in_damper_heat' not in obj.parameters:
                key_in = '11'
            obj.img_list[1] = img_data.dampers_img[key_in]
        else:
            obj.img_list[1] = ''
    return 1000


def filters(obj):
    if obj.system_type == 'In_out':
        if 'filt_in' in obj.parameters:
            if 'in_filter_quantity' in obj.numer_param:
                variant = [3, 11, 12]
                for i in variant[:int(obj.numer_param['in_filter_quantity'])+1]:
                    obj.img_list[i] = img_data.filters_img['0']
                for i in variant[int(obj.numer_param['in_filter_quantity'])+1:]:
                    obj.img_list[i] = ''
        elif "filt_in" not in obj.parameters:
            obj.img_list[3], obj.img_list[11], obj.img_list[12] = '', '', ''
        if 'filt_out' in obj.parameters:
            obj.img_list[10] = img_data.filters_img['1']
        elif 'filt_out' not in obj.parameters:
            obj.img_list[10] = ''
    elif obj.system_type == 'In':
        if 'filt_in' in obj.parameters:
            if 'in_filter_quantity' in obj.numer_param:
                variant = [3, 9, 10]
                for i in variant[:int(obj.numer_param['in_filter_quantity'])+1]:
                    obj.img_list[i] = img_data.filters_img['2']
                for i in variant[int(obj.numer_param['in_filter_quantity'])+1:]:
                    obj.img_list[i] = ''
        elif "filt_in" not in obj.parameters:
            obj.img_list[3], obj.img_list[9], obj.img_list[10] = '', '', ''
    if 'filt_in' in obj.parameters or 'filt_out' in obj.parameters:
        return 1000
    return 0


def cabinet(obj):
    if obj.system_type == "In_out":
        if "switch_type" in obj.parameters:
            obj.img_list[17] = img_data.cabinet_img['1']
        else:
            obj.img_list[17] = img_data.cabinet_img['0']
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[13] = img_data.cabinet_img['2']
            obj.plc.add_signals(di=1)
        else:
            obj.img_list[13] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            obj.img_list[0] = img_data.cabinet_img['4']
        else:
            obj.img_list[0] = img_data.cabinet_img['3']
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[20] = img_data.cabinet_img['6']
        else:
            obj.img_list[20] = img_data.cabinet_img['5']
        if 'sensor_humid' in obj.parameters:
            obj.img_list[18] = img_data.cabinet_img['7']
        else:
            obj.img_list[18] = ''
        if 'sensor_hood' in obj.parameters:
            obj.img_list[19] = img_data.cabinet_img['8']
        else:
            obj.img_list[19] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[14] = img_data.cabinet_img['9']
        else:
            obj.img_list[14] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[15] = img_data.cabinet_img['10']
        else:
            obj.img_list[15] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[16] = img_data.cabinet_img['11']
        else:
            obj.img_list[16] = ''
    elif obj.system_type == 'In':
        if "switch_type" in obj.parameters:
            obj.img_list[15] = img_data.cabinet_img['13']
        else:
            obj.img_list[15] = img_data.cabinet_img['12']
        if 'shutdown_fire_signal' in obj.parameters:
            obj.img_list[11] = img_data.cabinet_img['14']
        else:
            obj.img_list[11] = ''
        if 'sensor_temp_outdoor' in obj.parameters:
            obj.img_list[0] = img_data.cabinet_img['16']
        else:
            obj.img_list[0] = img_data.cabinet_img['15']
        if 'sensor_temp_indoor' in obj.parameters:
            obj.img_list[17] = img_data.cabinet_img['17']
        else:
            obj.img_list[17] = img_data.cabinet_img['18']
        if 'sensor_humid' in obj.parameters:
            obj.img_list[16] = img_data.cabinet_img['19']
        else:
            obj.img_list[16] = ''
        if 'signal_work' in obj.parameters:
            obj.img_list[12] = img_data.cabinet_img['20']
        else:
            obj.img_list[12] = ''
        if 'signal_alarm' in obj.parameters:
            obj.img_list[13] = img_data.cabinet_img['21']
        else:
            obj.img_list[13] = ''
        if 'remote_control' in obj.parameters:
            obj.img_list[14] = img_data.cabinet_img['22']
        else:
            obj.img_list[14] = ''
    return 1000


def vent_power_in(obj):
    if int(obj.numer_param['vent_power_in']) <= 5:
        br_id = 3
    elif 5 < int(obj.numer_param['vent_power_in']) < 9:
        br_id = 2
    elif int(obj.numer_param['vent_power_in']) >= 9:
        br_id = 1
    print(br_id)
    breaker = db_handler.breaker_price((br_id,), obj.data_base)
    print(breaker)
    obj.specification.append(db_handler.breaker_obj((br_id,), obj.data_base))
    breaker += 2 * db_handler.breaker_price((5,), obj.data_base)
    obj.specification.append(db_handler.breaker_obj((5,), obj.data_base))
    if 'FC_in' in obj.parameters:
        power_price = db_handler.fc_price((int(obj.numer_param['vent_power_in']) + 1, ), obj.data_base)
        obj.specification.append(db_handler.fc_obj((int(obj.numer_param['vent_power_in']) + 1,), obj.data_base))
    else:
        if int(obj.numer_param['vent_power_in']) <= 8:
            cont_id = 1
        elif 8 < int(obj.numer_param['vent_power_in']) <= 14:
            cont_id = int(obj.numer_param['vent_power_in']) - 7
        else:
            cont_id = 7
        power_price = db_handler.contactor_price((cont_id, ), obj.data_base)
        obj.specification.append(db_handler.contactor_obj((cont_id,), obj.data_base))
    if 'dif_in' in obj.parameters:
        dif = db_handler.diff_price(obj.data_base)
        dif += db_handler.relay_price(obj.data_base)
        obj.specification.append(db_handler.diff_obj(obj.data_base))
        for i in db_handler.relay_obj(obj.data_base):
            obj.specification.append(i)
        obj.plc.add_signals(di=1)
    else:
        dif = 0
    relay = 2 * db_handler.relay_price(obj.data_base)
    for i in db_handler.relay_obj(obj.data_base):
        obj.specification.append(i)
    for i in db_handler.relay_obj(obj.data_base):
        obj.specification.append(i)
    return power_price + dif + breaker + relay


def vent_power_out(obj):
    if int(obj.numer_param['vent_power_out']) <= 5:
        br_id = 3
    elif 5 < int(obj.numer_param['vent_power_out']) < 9:
        br_id = 2
    elif int(obj.numer_param['vent_power_out']) >= 9:
        br_id = 1
    breaker = db_handler.breaker_price((br_id,), obj.data_base)
    obj.specification.append(db_handler.breaker_obj((br_id, ), obj.data_base))
    breaker += 2 * db_handler.breaker_price((5,), obj.data_base)
    obj.specification.append(db_handler.breaker_obj((5,), obj.data_base))
    if 'FC_out' in obj.parameters:
        power_price = db_handler.fc_price((int(obj.numer_param['vent_power_out']) + 1, ), obj.data_base)
        obj.specification.append(db_handler.fc_obj((int(obj.numer_param['vent_power_out']) + 1, ), obj.data_base))
    else:
        if int(obj.numer_param['vent_power_out']) <= 8:
            cont_id = 1
        elif 8 < int(obj.numer_param['vent_power_out']) <= 14:
            cont_id = int(obj.numer_param['vent_power_out']) - 7
        else:
            cont_id = 7
        power_price = db_handler.contactor_price((cont_id, ), obj.data_base)
        obj.specification.append(db_handler.contactor_obj((cont_id,), obj.data_base))
    if 'dif_out' in obj.parameters:
        dif = db_handler.diff_price(obj.data_base)
        dif += db_handler.relay_price(obj.data_base)
        obj.specification.append(db_handler.diff_obj(obj.data_base))
        for i in db_handler.relay_obj(obj.data_base):
            obj.specification.append(i)
        obj.plc.add_signals(di=1)
    else:
        dif = 0
    relay = 2 * db_handler.relay_price(obj.data_base)
    for i in db_handler.relay_obj(obj.data_base):
        obj.specification.append(i)
    for i in db_handler.relay_obj(obj.data_base):
        obj.specification.append(i)
    return power_price + dif + breaker + relay


def type_handling(system_type):
    if system_type == "In_out":
        return {"FC_in": "true", "FC_out": "true", "vent_power_in": '0', "vent_power_out": '0', 'shutdown_fire_signal': 'true'}
    elif system_type == "In":
        return {"FC_in": "true", "vent_power_in": '0', 'shutdown_fire_signal': 'true'}
    elif system_type == "Out":
        return {'FC_out': 'true', "vent_power_out": '0', 'shutdown_fire_signal': 'true'}


