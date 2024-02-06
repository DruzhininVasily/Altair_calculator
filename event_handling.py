import img_data


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
    img_list[7] = img_data.vent_in_img[key]
    return 1000


def vent_out(system_type, parameters, num_param, img_list):
    index = 8 if system_type == 'In_out' else 7
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
    return 1000


def first_heater(system_type, parameters, num_param, img_list):
    if 'select_0' not in parameters:
        for i in range(0, 4):
            img_list[i+3] = ''
    if system_type == "In_out":
        if 'first_heater_type' not in parameters:
            if 'select_0' in parameters and 'first_confirm' in parameters:
                key = '0'
            elif 'select_0' in parameters and 'first_confirm' not in parameters:
                key = '1'
            if 'first_thermostat' in parameters:
                img_list[4] = img_data.heater_img['10']
            else:
                img_list[4] = ''
        elif 'first_heater_type' in parameters:
            img_list[4] = ''
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
                img_list[4] = img_data.heater_img['11']
            else:
                img_list[4] = ''
        elif 'first_heater_type' in parameters:
            img_list[4] = ''
            if 'select_0' in parameters and 'first_electrical_thermal' in num_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[num_param['first_electrical_thermal']]
    img_list[3] = img_data.heater_img[key]
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
                img_list[6] = img_data.heater_img['10']
            else:
                img_list[6] = ''
        elif 'second_heat_choice' in parameters and 'second_heat_type' in parameters:
            img_list[6] = ''
            if 'select_0' in parameters and 'second_electrical_thermal' in num_param:
                variant = {'0': '2', '1': '3', '2': '4'}
                key = variant[num_param['second_electrical_thermal']]
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
                img_list[6] = img_data.heater_img['11']
            else:
                img_list[6] = ''
        elif 'second_heat_choice' in parameters and 'second_heat_type' in parameters:
            img_list[6] = ''
            if 'select_0' in parameters and 'second_electrical_thermal' in num_param:
                variant = {'0': '7', '1': '8', '2': '9'}
                key = variant[num_param['second_electrical_thermal']]
    img_list[5] = img_data.heater_img[key]
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
