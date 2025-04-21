document.addEventListener('DOMContentLoaded', function(){
    let typeSystem = null

    let messageData = {
        select_0: "false",
        select_1: "false",
        select_2: "false",
        damp_in: "false",
        damp_out: "false",
        filt_in: "false",
        filt_out: "false",
        res_in: "false",
        res_out: "false",
        humid_alarm: 'false',
        voltage_vent_in: "380",
        voltage_vent_out: "380",
        vent_quant_in: '0',
        vent_quant_out: '0',
        reserv_in: 'no_reserv',
        reserv_out: 'no_reserv',
        damp_vent_quant_in: '0',
        damp_vent_quant_out: '0',
        quant_dif_in: '1',
        quant_dif_out: '1',
        vent_damp_type_in: '0',
        vent_damp_type_out: '0',
        damp_vent_voltage_in: 'false',
        vent_damp_confirm_in: 'false',
        vent_damp_heat_in: 'false',
        vent_damp_heat_voltage_in: 'false',
        vent_damp_heat_power_in: '0',
        damp_vent_voltage_out: 'false',
        vent_damp_confirm_out: 'false',
        vent_damp_heat_out: 'false',
        vent_damp_heat_voltage_out: 'false',
        vent_damp_heat_power_out: '0',
        FC_in: "FC",
        pressure_maint_in: "false",
        pressure_maint_out: "false",
        FC_out: "FC",
        vent_termo_protect_in: 'no_protect',
        vent_termo_protect_out: 'no_protect',
        dif_in: "false",
        dif_out: "false",
        smooth_in: 'false',
        smooth_out: 'false',
        vent_power_in: "0",
        vent_power_out: "0",
        first_heater_type: "false",
        first_pump: "false",
        first_signal: "false",
        first_sensor: "false",
        first_thermostat: "false",
        first_thermostat_quant: '1',
        first_thermostat_length: '1',
        first_pump_voltage: "false",
        first_valve_voltage: "false",
        first_steps: "0",
        electrical_first_step_power: "0",
        electrical_first_step_signal: "false",
        first_electrical_thermal: "0",
        add_thermo_sensor: 'false',
        second_heat_choice: "false",
        second_heat_type: "false",
        second_pump: "false",
        second_signal: "false",
        second_sensor: "false",
        second_thermostat: "false",
        second_thermostat_quant: '1',
        second_thermostat_length: '1',
        second_pump_voltage: "false",
        second_valve_voltage: "false",
        second_steps: "0",
        electrical_second_step_power: "0",
        electrical_second_step_signal: "false",
        second_electrical_thermal: "0",
        in_damper_voltage: 'false',
        in_damper_type: '0',
        in_damper_confirm: 'false',
        in_damper_heat: 'false',
        in_damper_heat_voltage: 'false',
        in_damper_heat_power: '0',
        out_damper_voltage: 'false',
        out_damper_type: '0',
        out_damper_confirm: 'false',
        out_damper_heat: 'false',
        out_damper_heat_voltage: 'false',
        out_damper_heat_power: '0',
        in_filter_quantity: '0',
        out_filter_quantity: '0',
        in_hepa_filter: 'false',
        out_hepa_filter: 'false',
        filt_in_indication: 'false',
        filt_out_indication: 'false',
        switch_type: 'false',
        base_controller: '0',
        shutdown_fire_signal: 'false',
        sensor_temp_outdoor: 'false',
        sensor_temp_indoor: 'false',
        sensor_temp_outdoor_type: 'outdoor',
        sensor_humid: 'false',
        sensor_hood_in: 'false',
        sensor_hood_out: 'false',
        signal_work: 'false',
        signal_alarm: 'false',
        touchpad: 'false',
        remote_control: 'false',
        cool_alarm: 'false',
        cool_type: 'frion',
        disp_protocol: '1',
        add_signals: 'false',
        di_signal: '0',
        do_signal: '0',
        ai_signal: '0',
        ao_signal: '0',
        pt_signal: '0',
    }

    let refButtons = {
        heaters: "select_0",
        coolers: "select_1",
        dehumids: "select_2",
        dampers: ["damp_in", 'damp_out'],
        filters: ["filt_in", "filt_out"],
        reserve: ["res_in", "res_out"]
    };

    let heaterFirstBoolDefault = {
        first_heater_type: 'false',
        first_pump: 'true',
        first_signal: 'true',
        first_sensor: 'true',
        first_thermostat: 'true',
        first_pump_voltage: 'false',
        first_valve_voltage: 'false',
        electrical_first_step_signal: 'false',
        second_heat_choice: 'false',
        sensor_temp_outdoor: 'true',
        sensor_hood_in: 'true',
        };

    let heaterSecondBoolDefault = {
        second_heat_type: 'false',
        second_pump: 'true',
        second_signal: 'true',
        second_sensor: 'false',
        second_thermostat: 'false',
        second_pump_voltage: 'false',
        second_valve_voltage: 'false',
        electrical_second_step_signal: 'false'
    }

    let heaterDecDefault = {
        first_steps: '0',
        electrical_first_step_power: '0',
        first_electrical_thermal: '0',
        second_steps: '0',
        electrical_second_step_power: '0',
        second_electrical_thermal: '0'
    }

    let dampInDefault = {
        in_damper_voltage: 'false',
        in_damper_type: '0',
        in_damper_confirm: 'false',
        in_damper_heat: 'false',
        in_damper_heat_voltage: 'false',
        in_damper_heat_power: '0'
    };

    let dampOutDefault = {
        out_damper_voltage: 'false',
        out_damper_type: '0',
        out_damper_confirm: 'false',
        out_damper_heat: 'false',
        out_damper_heat_voltage: 'false',
        out_damper_heat_power: '0'
    }

    let defaultNumeric = {
        vent_power_in: '0',
        vent_power_out: '0',
        vent_quant_in: '1',
        vent_quant_out: '1',
        first_steps: '0',
        electrical_first_step_power: '0',
        first_electrical_thermal: '0',
        second_steps: '0',
        electrical_second_step_power: '0',
        second_electrical_thermal: '0',
        in_damper_heat_power: '0',
        out_damper_heat_power: '0',
        in_filter_quantity: '0',
        out_filter_quantity: '0',
        base_controller: '0',
        in_damper_type: '0',
        out_damper_type: '0',
        FC_in: "FC",
        FC_out: "FC",
        damp_vent_quant_in: "0",
        damp_vent_quant_out: '0',
        quant_dif_in: '1',
        quant_dif_out: '1',
        vent_damp_type_in: '0',
        vent_damp_type_out: '0',
        voltage_vent_in: '380',
        voltage_vent_out: '380',
        vent_termo_protect_in: 'no_protect',
        vent_termo_protect_out: 'no_protect',
        vent_damp_heat_power_in: '0',
        reserv_in: 'no_reserv',
        reserv_out: 'no_reserv',
        first_thermostat_quant: '1',
        first_thermostat_length: '1',
        second_thermostat_quant: '1',
        second_thermostat_length: '1',
        cool_type: 'frion',
        sensor_temp_outdoor_type: 'outdoor',
        disp_protocol: '1',
        di_signal: '0',
        do_signal: '0',
        ai_signal: '0',
        ao_signal: '0',
        pt_signal: '0'
    }

    let = powerData = {0: "0.75", 1: "1.5", 2: "2.2", 3: "4", 4: "5.5", 5: "7.5", 6: "11", 7: "15", 8: "18.5", 9: "22", 10: "30", 11: "37", 12: "45", 13: '55'}
    let = powerDamperHeatData = {0: "0.1", 1: "0.2", 2: "0.3", 3: "0.4", 4: "0.5", 5: "0.6", 6: "0.7", 7: "0.8", 8: "0.9", 9: "1.0", 10: "1.1", 11: "1.2"}
    let = powerHeatData = {0: '3', 1: '6', 2: '9', 3: '12', 4: '15'}

    let price = document.querySelector("#price");
    let systemType = document.querySelectorAll(".radio input")
    let specButton = document.querySelector("#spec")

    let wsUrl = document.URL.split('//')
    let protocol = 'ws://'
    if (wsUrl[0] == 'https:'){
        protocol = 'wss://';
    }


    let websocketClient  = new WebSocket(protocol+wsUrl[1].split('/:')[0]);

// Функция для обработки input type="select" на основном экране

    let selectFunc = function (index, e) {
        selIndex = {0: "select_0", 1: "select_1", 2: "select_2"}
        try {
            e = e.target.value
        } catch (err) {
            e = e.value
        }
        messageData[selIndex[index]] = e
        if (e == 'false') {
            switch (index) {
                case 0:
                    for (key in heaterFirstBoolDefault) {
                        messageData[key] = 'false';
                    };
                    for (key in heaterSecondBoolDefault) {
                        messageData[key] = 'false';
                    };
                    for (key in heaterDecDefault) {
                        messageData[key] = '0';
                    };
                    break
                case 1:
                    messageData['cool_alarm'] = 'false';
                    break
                case 2:
                    messageData['select_1'] = 'false'
                    messageData['select_0'] = 'false'
                    messageData['second_heat_choice'] = 'false'
            };
            hideParameters()
        }
        else {
            switch (index) {
                case 0:
                    for (key in heaterFirstBoolDefault) {
                        messageData[key] = heaterFirstBoolDefault[key];
                    };
                    for (key in heaterDecDefault) {
                        messageData[key] = heaterDecDefault[key];
                    };
                    document.getElementsByClassName('electrical_first_container')[0].classList.add('disabled');
                    document.getElementsByClassName('water_first_container')[0].classList.remove('disabled');
                    document.getElementsByClassName('second_container')[0].classList.add('disabled');
                    document.getElementsByClassName('electrical_second_container')[0].classList.add('disabled');
                    document.getElementsByClassName('water_second_container')[0].classList.remove('disabled');
                    document.getElementsByClassName('heater_type_first')[0].value = 'false';
                    document.getElementsByClassName('heater_type_second')[0].value = 'false';
                    document.getElementsByClassName('second_heat_choice')[0].checked = false;
                    break
                case 1:
                    messageData['cool_alarm'] = 'false'
                    document.getElementById('cool_alarm').checked = false;
                    break
                case 2:
                    let cooler = document.querySelector('.cool_action')
                    let heat = document.querySelector('.heater_action')
                    let secondHeat = document.querySelector('.second_heat_choice')
                    cooler.value = 'true'
                    heat.value = 'true'
                    secondHeat.checked = true
                    messageData['select_1'] = 'true'
                    messageData['select_0'] = 'true'
                    messageData['second_heat_choice'] = 'true'
                    messageData['sensor_temp_outdoor'] = 'true'
                    messageData['sensor_hood_in'] = 'true'
                    messageData['sensor_humid'] = 'true'
                    messageData['first_pump'] = 'true'
                    messageData['first_signal'] = 'true'
                    messageData['first_sensor'] = 'true'
                    messageData['second_pump'] = 'true'
                    messageData['second_signal'] = 'true'
                    messageData['add_thermo_sensor'] = 'true'
            };
        }
        websocketClient.send(JSON.stringify(messageData));
    };

// Включение селектов

    let onSelect = function () {
        let sel = document.querySelectorAll(".select");
        for (let i=0; i<sel.length; i++) {
            sel[i].removeAttribute('disabled');
            sel[i].selectedIndex = 0;
            sel[i].addEventListener('change', () => selectFunc(i, event))
        };
    };

// Выключение селектов

    let offSelect = function () {
        let sel = document.querySelectorAll(".select");
        for (let i=0; i<sel.length; i++) {
            sel[i].selectedIndex = 0;
            sel[i].setAttribute('disabled', 'disabled')
        };
    };

    // Функция для добавления обработчиков к выбору обогрева задвижек

    let DampersHeatChoice = function (e, heatContainer, damperRange, damperSelect, damperSpan, dampHeatPower, dampHeatVoltage) {
        let DamperHeatContainer = document.querySelector(heatContainer)
        if (e.target) {
            e = e.target
        }
        else {
            e = e
        }
            if (e.checked == true) {
                DamperHeatContainer.classList.remove('disabled')
                addListeners(['', '', damperRange, damperSelect], damperSpan, '')
                messageData[e.name] = 'true';
                websocketClient.send(JSON.stringify(messageData));
            }
            else if (e.checked == false) {
                DamperHeatContainer.classList.add('disabled');
                document.getElementById(dampHeatPower).value = '0';
                document.getElementById(dampHeatVoltage).value = 'false';
                messageData[dampHeatPower] = '0';
                messageData[dampHeatVoltage] = 'false';
                messageData[e.name] = 'false';
                websocketClient.send(JSON.stringify(messageData));
            };
    };

// Включение чекбоксов на главном экране

    let onCheck = function(cl) {
        let elements = document.querySelectorAll(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 1;";
            elements[index].removeAttribute('disabled');
            elements[index].checked = false;
            elements[index].onclick = () => {
                switch(index) {
                    case 0:
                        if (elements[index].checked == false) {
                            if (elements[index].id == 'damp_in') {
                                let inDamperContainer = document.querySelector('.in_damper_container');
                                let inDamperHeatContainer = document.querySelector('.in_damper_heat_parameter_container')
                                inDamperHeatContainer.classList.add('disabled');
                                inDamperContainer.classList.add('disabled');
                                for (el in dampInDefault) {
                                    messageData[el] = dampInDefault[el];
                                };
                            }
                            else if (elements[index].id == 'damp_out') {
                                let outDamperContainer = document.querySelector('.out_damper_container');
                                let outDamperHeatContainer = document.querySelector('.out_damper_heat_parameter_container')
                                outDamperHeatContainer.classList.add('disabled');
                                outDamperContainer.classList.add('disabled');
                                for (el in dampOutDefault) {
                                    messageData[el] = dampOutDefault[el];
                                };
                            };
                        }
                        else if (elements[index].checked == true) {
                            if (elements[index].id == 'damp_in') {
                                let inDamperContainer = document.querySelector('.in_damper_container');
                                inDamperContainer.classList.remove('disabled');
                                for (el in dampInDefault) {
                                    if (document.getElementsByClassName(el)[0].type == 'checkbox') {
                                        document.getElementsByClassName(el)[0].checked = false;
                                    }
                                    else if (document.getElementsByClassName(el)[0].type == 'range') {
                                        document.getElementsByClassName(el)[0].value = '0';
                                    }
                                    else {
                                        if (el == 'in_damper_type') {
                                            document.getElementsByClassName(el)[0].value = '0'
                                        }
                                        else {
                                            document.getElementsByClassName(el)[0].value = 'false'
                                        }
                                    };
                                };
                                addListeners(['', '.in_damper_checkbox', '', '.in_damper_select', '', '']);
                                let inDamperHeatChoice = document.querySelector('.in_damper_heat')
                                inDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.in_damper_heat_parameter_container', '.in_damper_heat_range', '.in_damper_heat_select', '', 'in_damper_heat_power', 'in_damper_heat_voltage'));
                            }
                            else if (elements[index].id == 'damp_out') {
                                let outDamperContainer = document.querySelector('.out_damper_container');
                                outDamperContainer.classList.remove('disabled');
                                for (el in dampOutDefault) {
                                   if (document.getElementsByClassName(el)[0].type == 'checkbox') {
                                        document.getElementsByClassName(el)[0].checked = false;
                                    }
                                    else if (document.getElementsByClassName(el)[0].type == 'range') {
                                        document.getElementsByClassName(el)[0].value = '0';
                                    }
                                    else {
                                        if (el == 'out_damper_type') {
                                            document.getElementsByClassName(el)[0].value = '0'
                                        }
                                        else {
                                            document.getElementsByClassName(el)[0].value = 'false'
                                        }
                                    };
                                };
                                addListeners(['', '.out_damper_checkbox', '', '.out_damper_select', '', '']);
                                let outDamperHeatChoice = document.querySelector('.out_damper_heat');
                                outDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.out_damper_heat_parameter_container', '.out_damper_heat_range', '.out_damper_heat_select', '', 'out_damper_heat_power', 'out_damper_heat_voltage'));
                            };
                        }
                    case 1:
                        if (elements[index].checked == false) {
                            if (elements[index].id == 'filt_in') {
                                let inFilterContainer = document.querySelector('.in_filter');
                                inFilterContainer.classList.add('disabled');
                                messageData['in_filter_quantity'] = '0'
                            }
                            else if (elements[index].id == 'filt_out') {
                                let outFilterContainer = document.querySelector('.out_filter');
                                outFilterContainer.classList.add('disabled');
                                messageData['out_filter_quantity'] = '0';
                            };
                        }
                        else if (elements[index].checked == true) {
                            if (elements[index].id == 'filt_in') {
                                let inFilterContainer = document.querySelector('.in_filter');
                                inFilterContainer.classList.remove('disabled');
                                document.getElementsByClassName('in_filter_quantity')[0].value = '0'
                                addListeners(['', '', '', '.in_filter_select', '', '']);
                            }
                            else if (elements[index].id == 'filt_out') {
                                let outFilterContainer = document.querySelector('.out_filter');
                                outFilterContainer.classList.remove('disabled');
                                document.getElementsByClassName('out_filter_quantity')[0].value = '0'
                                addListeners(['', '', '', '.out_filter_select', '', '']);
                            };
                        }
                }
                messageData[elements[index].id] = String(elements[index].checked)
                websocketClient.send(JSON.stringify(messageData));
            }
        };
    };

// Выключение чекбоксов

    let offCheck = function(cl) {
        let elements = document.querySelectorAll(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 0;";
            elements[index].setAttribute('disabled', 'disabled');
        };
    };

// Универсальная функция для отправки данных на сервер и регистрации изменений

    let sendData = function (name, val) {
        messageData[name] = val;
        websocketClient.send(JSON.stringify(messageData));
    }

// Функция для добавки обработчиков в окне параметров

    let addListeners = function (array, outValue, dataSet) {
        let radioObjects = array[0]!='' ? document.querySelectorAll(array[0]) : [];
        let checkObjects = array[1]!='' ? document.querySelectorAll(array[1]) : [];
        let rangeObjects = array[2]!='' ? document.querySelectorAll(array[2]) : [];
        let selectObjects = array[3]!='' ? document.querySelectorAll(array[3]) : [];
        let rangeOut = outValue!='' ? document.querySelector(outValue) : document.querySelector('#test');
        for (let index=0; index<radioObjects.length; index++) {
            if (radioObjects[index].classList.contains('default')) {
                if (messageData[radioObjects[index].name] == 'false') {
                    radioObjects[index].checked = true;
                }
                else if (messageData[radioObjects[index].name] == 'FC') {
                    radioObjects[index].checked = true;
                }
            }
            else {
                if (messageData[radioObjects[index].name] == "true")
                {radioObjects[index].checked = true;}
                else if (messageData[radioObjects[index].name] == radioObjects[index].value)
                {radioObjects[index].checked = true;}
                else {radioObjects[index].checked = false;}
            }
            radioObjects[index].addEventListener('change', function(e) {
                sendData(radioObjects[index].name, radioObjects[index].value);
            });
        };
        for (let index=0; index<checkObjects.length; index++) {
            if (messageData[checkObjects[index].name] == "false"){
            checkObjects[index].checked = false;
            }
            else {checkObjects[index].checked = true;}
            checkObjects[index].addEventListener('click', function(e) {
                sendData(checkObjects[index].name, String(checkObjects[index].checked))
            });
        };
        for (let index=0; index<rangeObjects.length; index++) {
            rangeOut.textContent = dataSet[messageData[rangeObjects[index].name]]
            rangeObjects[index].value = messageData[rangeObjects[index].name];
            rangeObjects[index].addEventListener('change', function(e) {
                rangeOut.textContent = dataSet[rangeObjects[index].value]
                sendData(rangeObjects[index].name, rangeObjects[index].value)
            });
        };
        for (let index=0; index<selectObjects.length; index++) {
            selectObjects[index].value = messageData[selectObjects[index].name];
            selectObjects[index].addEventListener('change', function(e) {
                sendData(selectObjects[index].name, selectObjects[index].value)
            });
        };
    }

// Функция кнопки параметры вентилятора

    let ventsFunc = function() {
        let vent220In = document.querySelector('#in_220')
        let vent380In = document.querySelector('#in_380')
        let voltageInBlock = document.querySelector('.voltage_in_block')
        let voltageOutBlock = document.querySelector('.voltage_out_block')
        let vent220Out = document.querySelector('#out_220')
        let vent380Out = document.querySelector('#out_380')
        let fcInBlock = document.querySelector('.fc_in_block')
        let fcOutBlock = document.querySelector('.fc_out_block')
        let potentiometrInBlock = document.querySelector('.potentiometr_in_block')
        let potentiometrOutBlock = document.querySelector('.potentiometr_out_block')
        let potentiometrIn = document.querySelector('#potentiometr_in')
        let potentiometrOut = document.querySelector('#potentiometr_out')
        let paramVent_in = document.querySelector(".paramVent_in")
        let paramVent_out = document.querySelector(".paramVent_out")
        let fc_in = document.querySelector('#FC_in');
        let fc_out = document.querySelector('#FC_out');
        let ec_in = document.querySelector('#EC_in');
        let ec_out = document.querySelector('#EC_out');
        let ventTypeIn = document.querySelector('.vent_type_in')
        let ventTypeOut = document.querySelector('.vent_type_out')
        let ventReservIn = document.querySelector('#vent_reserv_in')
        let ventReservOut = document.querySelector('#vent_reserv_out')
        let motorReservIn = document.querySelector('#motor_reserv_in')
        let motorReservOut = document.querySelector('#motor_reserv_out')
        let reservContainerIn = document.querySelector('.vent_reserv_block_in')
        let reservContainerOut = document.querySelector('.vent_reserv_block_out')
        let ventDampQuantBlockIn = document.querySelector('.damp_vent_quant_in_block')
        let ventDampQuantBlockOut = document.querySelector('.damp_vent_quant_out_block')
        let ventDampHeatIn = document.querySelector('.vent_damp_heat_in')
        let ventDampHeatBlockIn = document.querySelector ('.vent_damp_heat_block_in')
        let ventDampHeatOut = document.querySelector('.vent_damp_heat_out')
        let ventDampHeatBlockOut = document.querySelector ('.vent_damp_heat_block_out')
        let smooth_in_container = document.querySelector('#smooth_in_container');
        let smooth_out_container = document.querySelector('#smooth_out_container');
        let smooth_in = document.querySelector('#smooth_in');
        let smooth_out = document.querySelector('#smooth_out');
        let maint_in_container = document.querySelector('#maint_in_container')
        let maint_out_container = document.querySelector('#maint_out_container')
        let maint_in = document.querySelector('#pressure_maint_in')
        let maint_out = document.querySelector('#pressure_maint_out')
        let difIn = document.querySelector('#dif_in')
        let difOut = document.querySelector('#dif_out')
        let quantDifInBlock = document.querySelector('.quant_dif_in_block')
        let quantDifOutBlock = document.querySelector('.quant_dif_out_block')
        if (typeSystem == "In_out") {
            paramVent_in.classList.remove('disabled');
            paramVent_out.classList.remove('disabled');
            addListeners(['.vent_radio_info_in', '.vent_check_info_in', '.vent_range_info_in', '.vent_quant_in'], "", powerData);
            addListeners(['.vent_radio_info_out', '.vent_check_info_out', '.vent_range_info_out', '.vent_quant_out'], "", powerData)
            voltageInBlock.onclick = () => {
                if (vent220In.checked == true) {
                    fc_in.checked = false
                    fcInBlock.classList.add('disabled')
                    smooth_in_container.classList.add('disabled');
                    maint_in_container.classList.add('disabled');
                    potentiometrInBlock.classList.remove('disabled')
                    potentiometrIn.checked = true
                    sendData(potentiometrIn.name, potentiometrIn.value)
                    smooth_in.checked = false
                    sendData(smooth_in.name, 'false')
                    maint_in.checked = false
                    sendData('pressure_maint_in', 'false')
                }
                else if (vent380In.checked == true) {
                    fc_in.checked = true
                    fcInBlock.classList.remove('disabled')
                    smooth_in_container.classList.remove('disabled');
                    potentiometrIn.checked = false
                    potentiometrInBlock.classList.add('disabled')
                    sendData(fc_in.name, fc_in.value)
                    maint_in.checked = false
                    sendData('pressure_maint_in', 'false')
                    maint_in_container.classList.add('disabled');
                }
            }
            voltageOutBlock.onclick = () => {
                if (vent220Out.checked == true) {
                    fc_out.checked = false
                    fcOutBlock.classList.add('disabled')
                    smooth_out_container.classList.add('disabled');
                    maint_out_container.classList.add('disabled');
                    potentiometrOutBlock.classList.remove('disabled')
                    potentiometrOut.checked = true
                    sendData(potentiometrOut.name, potentiometrOut.value)
                    smooth_out.checked = false
                    sendData(smooth_out.name, 'false')
                    maint_out.checked = false
                    sendData('pressure_maint_out', 'false')
                }
                else if (vent380Out.checked == true) {
                    fc_out.checked = true
                    fcOutBlock.classList.remove('disabled')
                    smooth_out_container.classList.remove('disabled');
                    potentiometrOut.checked = false
                    potentiometrOutBlock.classList.add('disabled')
                    sendData(fc_out.name, fc_out.value)
                    maint_out.checked = false
                    sendData('pressure_maint_out', 'false')
                    maint_out_container.classList.add('disabled');
                }
            }
            if (ventReservIn.checked == true) {
                ventDampQuantBlockIn.classList.remove('disabled');
                quantDifInBlock.classList.remove('disabled');
                addListeners(['', '', '', '.vent_in_reserv_selects'], '', powerData);
                difIn.checked = true;
                if (ventDampHeatIn.checked == true) {
                    ventDampHeatBlockIn.classList.remove('disabled')
                }
                else {ventDampHeatBlockIn.classList.add('disabled')}
                ventDampHeatIn.onclick = () => {
                    if (ventDampHeatIn.checked == true) {
                    ventDampHeatBlockIn.classList.remove('disabled')
                    }
                    else {ventDampHeatBlockIn.classList.add('disabled')}
                }
            }
            else {ventDampQuantBlockIn.classList.add('disabled')}
            reservContainerIn.onclick = () => {
                if (ventReservIn.checked == true) {
                    ventDampQuantBlockIn.classList.remove('disabled');
                    quantDifInBlock.classList.remove('disabled');
                    addListeners(['', '', '', '.vent_in_reserv_selects'], '', powerData)
                    difIn.checked = true;
                    sendData(difIn.name, 'true')
                    ventDampHeatIn.onclick = () => {
                        if (ventDampHeatIn.checked == true) {
                            ventDampHeatBlockIn.classList.remove('disabled')
                        }
                        else {ventDampHeatBlockIn.classList.add('disabled')}
                }
                }
                else if (motorReservIn.checked == true) {
                    ventDampQuantBlockIn.classList.add('disabled')
                    quantDifInBlock.classList.add('disabled');
                    difIn.checked = true;
                    sendData(difIn.name, 'true')
                }
                else {
                    ventDampQuantBlockIn.classList.add('disabled')
                    quantDifInBlock.classList.add('disabled');
                    difIn.checked = false
                    sendData(difIn.name, 'false')
                };
            }
            if (fc_in.checked == true) {
                smooth_in_container.classList.remove('disabled');
                addListeners(['', '.smooth_in', '', ''], '', powerData)
                smooth_in.onclick = () => {
                    if (smooth_in.checked == true) {
                        maint_in_container.classList.remove('disabled');
                    }
                    else {
                        maint_in_container.classList.add('disabled');
                        maint_in.checked = false
                        sendData('pressure_maint_in', 'false')
                    }
                }
            }
            else if (ec_in.checked == true) {
                smooth_in_container.classList.add('disabled');
                maint_in_container.classList.remove('disabled');
            }
            ventTypeIn.onclick = () => {
                if (fc_in.checked == true) {
                    smooth_in_container.classList.remove('disabled');
                    addListeners(['', '.smooth_in', '', ''], '', powerData)
                    if (smooth_in.checked == true) {
                        maint_in_container.classList.remove('disabled');
                    }
                    else {
                        maint_in_container.classList.add('disabled');
                        maint_in.checked = false
                        sendData('pressure_maint_in', 'false')
                    }
                    smooth_in.onclick = () => {
                        if (smooth_in.checked == true) {
                            maint_in_container.classList.remove('disabled');
                        }
                        else {
                            maint_in_container.classList.add('disabled');
                            maint_in.checked = false
                            sendData('pressure_maint_in', 'false')
                        }
                    }
                }
                else if (ec_in.checked == true) {
                    smooth_in_container.classList.add('disabled');
                    maint_in_container.classList.remove('disabled');
                }
                else {
                    smooth_in_container.classList.add('disabled');
                    maint_in_container.classList.add('disabled');
                    smooth_in.checked = false;
                    maint_in.checked = false;
                    sendData('pressure_maint_in', 'false')
                    sendData('smooth_in', 'false')
                }
            };
            if (ventReservOut.checked == true) {
                ventDampQuantBlockOut.classList.remove('disabled');
                quantDifOutBlock.classList.remove('disabled');
                addListeners(['', '', '', '.vent_out_reserv_selects'], '', powerData);
                difOut.checked = true;
                if (ventDampHeatOut.checked == true) {
                    ventDampHeatBlockOut.classList.remove('disabled')
                }
                else {ventDampHeatBlockOut.classList.add('disabled')}
                ventDampHeatIn.onclick = () => {
                    if (ventDampHeatOut.checked == true) {
                    ventDampHeatBlockOut.classList.remove('disabled')
                    }
                    else {ventDampHeatBlockOut.classList.add('disabled')}
                }
            }
            else {ventDampQuantBlockOut.classList.add('disabled')}
            reservContainerOut.onclick = () => {
                if (ventReservOut.checked == true) {
                    ventDampQuantBlockOut.classList.remove('disabled');
                    quantDifOutBlock.classList.remove('disabled');
                    addListeners(['', '', '', '.vent_out_reserv_selects'], '', powerData)
                    difOut.checked = true;
                    sendData(difOut.name, 'true')
                    ventDampHeatOut.onclick = () => {
                        if (ventDampHeatOut.checked == true) {
                            ventDampHeatBlockOut.classList.remove('disabled')
                        }
                        else {ventDampHeatBlockOut.classList.add('disabled')}
                    }
                }
                else if (motorReservOut.checked == true) {
                    ventDampQuantBlockOut.classList.add('disabled')
                    quantDifOutBlock.classList.add('disabled');
                    difOut.checked = true;
                    sendData(difOut.name, 'true')
                }
                else {
                    ventDampQuantBlockOut.classList.add('disabled')
                    quantDifOutBlock.classList.add('disabled');
                    difOut.checked = false
                    sendData(difOut.name, 'false')
                };
            }
            if (fc_out.checked == true) {
                smooth_out_container.classList.remove('disabled');
                    addListeners(['', '.smooth_out', '', ''], '', powerData)
                    if (smooth_out.checked == true) {
                        maint_out_container.classList.remove('disabled');
                    }
                    else {
                        maint_out_container.classList.add('disabled');
                        maint_out.checked = false
                        sendData('pressure_maint_out', 'false')
                    }
                    smooth_out.onclick = () => {
                        if (smooth_out.checked == true) {
                            maint_out_container.classList.remove('disabled');
                        }
                        else {
                            maint_out_container.classList.add('disabled');
                            maint_out.checked = false
                            sendData('pressure_maint_out', 'false')
                        }
                    }
            }
            else if (ec_out.checked == true) {
                maint_out_container.classList.remove('disabled');
                smooth_out_container.classList.add('disabled');
            }
            ventTypeOut.onclick = () => {
                if (fc_out.checked == true) {
                    smooth_out_container.classList.remove('disabled');
                    addListeners(['', '.smooth_out', '', ''], '', powerData)
                    smooth_out.onclick = () => {
                        if (smooth_out.checked == true) {
                            maint_out_container.classList.remove('disabled');
                        }
                        else {
                            maint_out_container.classList.add('disabled');
                            maint_out.checked = false
                            sendData('pressure_maint_out', 'false')
                        }
                    }
                }
                else if (ec_out.checked == true) {
                    maint_out_container.classList.remove('disabled');
                    smooth_out_container.classList.add('disabled');
                }
                else {
                    smooth_out_container.classList.add('disabled');
                    maint_out_container.classList.add('disabled');
                    maint_out.checked = false
                    sendData('pressure_maint_out', 'false')
                    smooth_out.checked = false;
                    sendData('smooth_out', 'false')
                }
            };
        }
        else if (typeSystem == "In") {
            paramVent_in.classList.remove('disabled');
            paramVent_out.className = ("paramVent_out hide_param disabled");
            addListeners(['.vent_radio_info_in', '.vent_check_info_in', '.vent_range_info_in', '.vent_quant_in'], "", powerData);
            voltageInBlock.onclick = () => {
                if (vent220In.checked == true) {
                    fc_in.checked = false
                    fcInBlock.classList.add('disabled')
                    potentiometrInBlock.classList.remove('disabled')
                    potentiometrIn.checked = true
                    sendData(potentiometrIn.name, potentiometrIn.value)
                }
                else if (vent380In.checked == true) {
                    fc_in.checked = true
                    fcInBlock.classList.remove('disabled')
                    potentiometrIn.checked = false
                    potentiometrInBlock.classList.add('disabled')
                    sendData(fc_in.name, fc_in.value)
                }
            }
            if (ventReservIn.checked == true) {
                ventDampQuantBlockIn.classList.remove('disabled');
                quantDifInBlock.classList.remove('disabled');
                addListeners(['', '', '', '.vent_in_reserv_selects'], '', powerData);
                difIn.checked = true;
            }
            else {ventDampQuantBlockIn.classList.add('disabled')}
            reservContainerIn.onclick = () => {
                if (ventReservIn.checked == true) {
                    ventDampQuantBlockIn.classList.remove('disabled');
                    quantDifInBlock.classList.remove('disabled');
                    addListeners(['', '', '', '.vent_in_reserv_selects'], '', powerData)
                    difIn.checked = true;
                    sendData(difIn.name, 'true')
                }
                else if (motorReservIn.checked == true) {
                    ventDampQuantBlockIn.classList.add('disabled')
                    quantDifInBlock.classList.add('disabled');
                    difIn.checked = true;
                    sendData(difIn.name, 'true')
                }
                else {
                    ventDampQuantBlockIn.classList.add('disabled')
                    quantDifInBlock.classList.add('disabled');
                    difIn.checked = false
                    sendData(difIn.name, 'false')
                };
            }
            if (fc_in.checked == true) {
                smooth_in_container.classList.remove('disabled');
                addListeners(['', '.smooth_in', '', ''], '', powerData)
                smooth_in.onclick = () => {
                    if (smooth_in.checked == true) {
                        maint_in_container.classList.remove('disabled');
                    }
                    else {
                        maint_in_container.classList.add('disabled');
                        maint_in.checked = false
                        sendData('pressure_maint_in', 'false')
                    }
                }
            }
            else if (ec_in.checked == true) {
                smooth_in_container.classList.add('disabled');
                maint_in_container.classList.remove('disabled');
            }
            ventTypeIn.onclick = () => {
                if (fc_in.checked == true) {
                    smooth_in_container.classList.remove('disabled');
                    addListeners(['', '.smooth_in', '', ''], '', powerData)
                    smooth_in.onclick = () => {
                        if (smooth_in.checked == true) {
                            maint_in_container.classList.remove('disabled');
                        }
                        else {
                            maint_in_container.classList.add('disabled');
                            maint_in.checked = false
                            sendData('pressure_maint_in', 'false')
                        }
                    }
                }
                else if (ec_in.checked == true) {
                    smooth_in_container.classList.add('disabled');
                    maint_in_container.classList.remove('disabled');
                }
                else {
                    smooth_in_container.classList.add('disabled');
                    maint_in_container.classList.add('disabled');
                    smooth_in.checked = false;
                    maint_in.checked = false;
                    sendData('pressure_maint_in', 'false')
                    sendData('smooth_in', 'false')
                }
            };
        }
        else if (typeSystem == "Out") {
            paramVent_out.classList.remove('disabled');
            paramVent_in.className = ("paramVent_in hide_param disabled");
            addListeners(['.vent_radio_info_out', '.vent_check_info_out', '.vent_range_info_out', '.vent_quant_out'], "", powerData);
            voltageOutBlock.onclick = () => {
                if (vent220Out.checked == true) {
                    fc_out.checked = false
                    fcOutBlock.classList.add('disabled')
                    potentiometrOutBlock.classList.remove('disabled')
                    potentiometrOut.checked = true
                    sendData(potentiometrOut.name, potentiometrOut.value)
                }
                else if (vent380Out.checked == true) {
                    fc_out.checked = true
                    fcOutBlock.classList.remove('disabled')
                    potentiometrOut.checked = false
                    potentiometrOutBlock.classList.add('disabled')
                    sendData(fc_out.name, fc_out.value)
                }
            }
            if (ventReservOut.checked == true) {
                ventDampQuantBlockOut.classList.remove('disabled');
                quantDifOutBlock.classList.remove('disabled');
                addListeners(['', '', '', '.vent_out_reserv_selects'], '', powerData);
                difOut.checked = true;
            }
            else {ventDampQuantBlockOut.classList.add('disabled')}
            reservContainerOut.onclick = () => {
                if (ventReservOut.checked == true) {
                    ventDampQuantBlockOut.classList.remove('disabled');
                    quantDifOutBlock.classList.remove('disabled');
                    addListeners(['', '', '', '.vent_out_reserv_selects'], '', powerData)
                    difOut.checked = true;
                    sendData(difOut.name, 'true')
                }
                else if (motorReservOut.checked == true) {
                    ventDampQuantBlockOut.classList.add('disabled')
                    quantDifOutBlock.classList.add('disabled');
                    difOut.checked = true;
                    sendData(difOut.name, 'true')
                }
                else {
                    ventDampQuantBlockOut.classList.add('disabled')
                    quantDifOutBlock.classList.add('disabled');
                    difOut.checked = false
                    sendData(difOut.name, 'false')
                };
            }
            if (fc_out.checked == true) {
                smooth_out_container.classList.remove('disabled');
                    addListeners(['', '.smooth_out', '', ''], '', powerData)
                    smooth_out.onclick = () => {
                        if (smooth_out.checked == true) {
                            maint_out_container.classList.remove('disabled');
                        }
                        else {
                            maint_out_container.classList.add('disabled');
                            maint_out.checked = false
                            sendData('pressure_maint_out', 'false')
                        }
                    }
            }
            else if (ec_out.checked == true) {
                maint_out_container.classList.remove('disabled');
                smooth_out_container.classList.add('disabled');
            }
            ventTypeOut.onclick = () => {
                if (fc_out.checked == true) {
                    smooth_out_container.classList.remove('disabled');
                    addListeners(['', '.smooth_out', '', ''], '', powerData)
                    smooth_out.onclick = () => {
                        if (smooth_out.checked == true) {
                            maint_out_container.classList.remove('disabled');
                        }
                        else {
                            maint_out_container.classList.add('disabled');
                            maint_out.checked = false
                            sendData('pressure_maint_out', 'false')
                        }
                    }
                }
                else if (ec_out.checked == true) {
                    maint_out_container.classList.remove('disabled');
                    smooth_out_container.classList.add('disabled');
                }
                else {
                    smooth_out_container.classList.add('disabled');
                    maint_out_container.classList.add('disabled');
                    maint_out.checked = false
                    sendData('pressure_maint_out', 'false')
                    smooth_out.checked = false;
                    sendData('smooth_out', 'false')
                }
            };
        };
    };

// Функция выбора типа нагревателя

    let typeHeatChoice = function (e, elClass, waterClass, list_water, list_elect) {
        let electricalContainer = document.querySelector(elClass);
        let waterContainer = document.querySelector(waterClass);
        if (e.target) {
            e = e.target
        }
        else {
            e = e
        }
        if (e.value == "true") {
                electricalContainer.classList.remove('disabled');
                waterContainer.classList.add('disabled');
                sendData(e.name, e.value);
                addListeners([list_elect[0], list_elect[1], list_elect[2], list_elect[3]], list_elect[4], list_elect[5]);
        }
        else {
                electricalContainer.classList.add('disabled');
                waterContainer.classList.remove('disabled');
                addListeners([list_water[0], list_water[1], list_water[2], list_water[3]], list_water[4], list_water[5])
                sendData(e.name, e.value);
        };
    }


// Функция для обработки окна нагреватели

    let heatersFunc = function () {
        let heatContainer = document.querySelector(".heat_container");
        let secondChoice = document.querySelector(".second_heat_choice");
        let firstTypeHeatChoice = document.querySelector('.heater_type_first')
        let waterFirstThermostat = document.querySelector('.water_first_thermostat')
        let firstThermostatOptionsBlock = document.querySelector('.first_thermostat_options_block')
        let waterSecondThermostat = document.querySelector('.water_second_thermostat')
        let secondThermostatOptionsBlock = document.querySelector('.second_thermostat_options_block')
        heatContainer.classList.remove('disabled');
        addListeners(['', '.add_thermo_sensor', '', ''], '', '')
        if (messageData['first_heater_type'] == 'true') {
            firstTypeHeatChoice[1].selected = true
            typeHeatChoice(firstTypeHeatChoice, '.electrical_first_container', '.water_first_container', ['', '.first_water_checkbox', '', '.first_water_select', '', ''], ['', '.first_electrical_checkbox', '.first_electrical_range', '.first_electrical_select', '', ''])
        }
        else {
            if (waterFirstThermostat.checked == true) {
                firstThermostatOptionsBlock.classList.remove('disabled')
                addListeners(['', '', '', '.first_thermostat_options'], '', powerData)
            }
            else {firstThermostatOptionsBlock.classList.add('disabled')}
            addListeners(['', '.first_water_checkbox', '', '.first_water_select'], '', '')
            waterFirstThermostat.onclick = () => {
                if (waterFirstThermostat.checked == true) {
                    firstThermostatOptionsBlock.classList.remove('disabled')
                    addListeners(['', '', '', '.first_thermostat_options'], '', powerData)
                }
                else {firstThermostatOptionsBlock.classList.add('disabled')}
            }
        }
        let secondContainer = document.querySelector(".second_container");
        let secondTypeHeatChoice = document.querySelector(".heater_type_second");
        firstTypeHeatChoice.addEventListener('change', () => typeHeatChoice(event, '.electrical_first_container', '.water_first_container', ['', '.first_water_checkbox', '', '.first_water_select', '', ''], ['', '.first_electrical_checkbox', '.first_electrical_range', '.first_electrical_select', '', '']));
        if (messageData['second_heat_choice'] == 'true') {
            secondChoice.checked = true;
            secondContainer.classList.remove('disabled');
            if (messageData['second_heat_type'] == 'true'){
                secondTypeHeatChoice[1].selected = true
                typeHeatChoice(secondTypeHeatChoice, '.electrical_second_container', '.water_second_container', ['', '.second_water_checkbox', '', '.second_water_select', '', ''], ['', '.second_electrical_checkbox', '.second_electrical_range', '.second_electrical_select', '', ''])
            }
            else {
            if (waterSecondThermostat.checked == true) {
                secondThermostatOptionsBlock.classList.remove('disabled')
                addListeners(['', '', '', '.second_thermostat_options'], '', powerData)
            }
            else {secondThermostatOptionsBlock.classList.add('disabled')}
            addListeners(['', '.second_water_checkbox', '', '.second_water_select'], '', '')
            waterSecondThermostat.onclick = () => {
                if (waterSecondThermostat.checked == true) {
                    secondThermostatOptionsBlock.classList.remove('disabled')
                    addListeners(['', '', '', '.second_thermostat_options'], '', powerData)
                }
                else {secondThermostatOptionsBlock.classList.add('disabled')}
                }
            }
        }
        secondChoice.onclick = () => {
            sendData(secondChoice.name, String(secondChoice.checked));
            if (secondChoice.checked == true) {
            secondContainer.classList.remove('disabled');
            messageData['second_pump'] = 'true';
            messageData['second_signal'] = 'true';
            addListeners(['', '.second_water_checkbox', '', '.second_water_select'], '', '')
            secondTypeHeatChoice.addEventListener('change', () => typeHeatChoice(event, '.electrical_second_container', '.water_second_container', ['', '.second_water_checkbox', '', '.second_water_select', '', ''], ['', '.second_electrical_checkbox', '.second_electrical_range', '.second_electrical_select', '', '']));
            if (messageData['second_heat_type'] != 'true'){
                if (waterSecondThermostat.checked == true) {
                    secondThermostatOptionsBlock.classList.remove('disabled')
                    addListeners(['', '', '', '.second_thermostat_options'], '', powerData)
                }
                else {secondThermostatOptionsBlock.classList.add('disabled')}
                addListeners(['', '.second_water_checkbox', '', '.second_water_select'], '', '')
                waterSecondThermostat.onclick = () => {
                    if (waterSecondThermostat.checked == true) {
                        secondThermostatOptionsBlock.classList.remove('disabled')
                        addListeners(['', '', '', '.second_thermostat_options'], '', powerData)
                    }
                    else {secondThermostatOptionsBlock.classList.add('disabled')}
                    }
                }
            }
            else {secondContainer.classList.add('disabled')};
        };
    }

    let dampersFunc = function (checkIn, checkOut) {
        hideParameters();
        let dampersContainer = document.querySelector('.dampers_container');
        dampersContainer.classList.remove('disabled');
        if (checkIn == 'true') {
            let inDamperContainer = document.querySelector('.in_damper_container');
            let inDamperHeatContainer = document.querySelector('.in_damper_heat_parameter_container');
            let inDamperHeatChoice = document.querySelector('.in_damper_heat')
            if (messageData['in_damper_heat'] == 'false'){
                inDamperHeatContainer.classList.add('disabled')
            }
            else {
                inDamperHeatChoice.checked = true
                DampersHeatChoice(inDamperHeatChoice, '.in_damper_heat_parameter_container', '.in_damper_heat_range', '.in_damper_heat_select', '', 'in_damper_heat_power', 'in_damper_heat_voltage')
            }
            inDamperContainer.classList.remove('disabled');
            addListeners(['', '.in_damper_checkbox', '', '.in_damper_select', '', ''])
            inDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.in_damper_heat_parameter_container', '.in_damper_heat_range', '.in_damper_heat_select', '', 'in_damper_heat_power', 'in_damper_heat_voltage'));
        }
        else if (checkIn == 'false') {
            let inDamperContainer = document.querySelector('.in_damper_container');
            inDamperContainer.classList.add('disabled');
        };
        if (checkOut == 'true') {
            let outDamperContainer = document.querySelector('.out_damper_container');
            let outDamperHeatContainer = document.querySelector('.out_damper_heat_parameter_container');
            let outDamperHeatChoice = document.querySelector('.out_damper_heat')
            if (messageData['out_damper_heat'] == 'false'){
                outDamperHeatContainer.classList.add('disabled')
            }
            else {
                outDamperHeatChoice.checked = true
                DampersHeatChoice(outDamperHeatChoice, '.out_damper_heat_parameter_container', '.out_damper_heat_range', '.out_damper_heat_select', '', 'out_damper_heat_power', 'out_damper_heat_voltage')
            }
            outDamperContainer.classList.remove('disabled');
            addListeners(['', '.out_damper_checkbox', '', '.out_damper_select', '', '']);
            outDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.out_damper_heat_parameter_container', '.out_damper_heat_range', '.out_damper_heat_select', '', 'out_damper_heat_power', 'out_damper_heat_voltage'));
        }
        else if (checkOut == 'false') {
            let outDamperContainer = document.querySelector('.out_damper_container');
            outDamperContainer.classList.add('disabled');
        };
    };

    let filtersFunc = function (checkIn, checkOut) {
        hideParameters();
        let filtersContainer = document.querySelector('.filters_container');
        filtersContainer.classList.remove('disabled');
        if (checkIn == 'true') {
            let inFilterContainer = document.querySelector('.in_filter');
            inFilterContainer.classList.remove('disabled');
            addListeners(['', '', '', '.in_filter_select', '', ''])
        }
        else if (checkIn == 'false') {
            let inFilterContainer = document.querySelector('.in_filter');
            inFilterContainer.classList.add('disabled');
        };
        if (checkOut == 'true') {
            let outFilterContainer = document.querySelector('.out_filter');
            outFilterContainer.classList.remove('disabled');
            addListeners(['', '', '', '.out_filter_select', '', '']);
        }
        else if (checkOut == 'false') {
            let outFilterContainer = document.querySelector('.out_filter');
            outFilterContainer.classList.add('disabled');
        };
        addListeners(['', '.filters_checkbox', '', '', '', '']);
    };

    let cabinetFunc = function () {
        hideParameters();
        let cabinetContainer = document.querySelector('.cabinet_container');
        cabinetContainer.classList.remove('disabled');
        addListeners(['', '.cabinet_checkbox', '', '.cabinet_select', '', '']);
        let sensor_hood_in_block = document.querySelector('.sensor_hood_in_block')
        let sensor_hood_out_block = document.querySelector('.sensor_hood_out_block')
        let sensor_humid = document.getElementById('sensor_humid')
        let sensor_temp_outdoor = document.querySelector('.sensor_temp_outdoor')
        let sensor_temp_outdoor_type_block = document.querySelector('.sensor_temp_outdoor_type_block')
        let sensor_temp_outdoor_type = document.querySelector('.sensor_temp_outdoor_type')
        let addSignals = document.querySelector('.add_signals')
        let addSignalsBlock = document.querySelector('.add_signals_block')
        if (addSignals.checked == true) {
            addSignalsBlock.classList.remove('disabled')
        }
        else {addSignalsBlock.classList.add('disabled')}
        addSignals.onclick = () => {
            if (addSignals.checked == true) {
                addSignalsBlock.classList.remove('disabled')
            }
            else {addSignalsBlock.classList.add('disabled')}
        }
        if (typeSystem == 'Out') {
            sensor_hood_in_block.classList.add('disabled')
            sensor_hood_out_block.classList.remove('disabled')
            sensor_humid.setAttribute('disabled', 'disabled')
        }
        else if (typeSystem == 'In') {
            sensor_hood_out_block.classList.add('disabled')
            sensor_hood_in_block.classList.remove('disabled')
            sensor_humid.removeAttribute("disabled")
        }
        else if (typeSystem == 'In_out') {
            sensor_humid.removeAttribute("disabled")
            sensor_hood_out_block.classList.remove('disabled')
            sensor_hood_in_block.classList.remove('disabled')
        }
        if (sensor_temp_outdoor.checked == true) {
            sensor_temp_outdoor_type_block.classList.remove('disabled')
        }
        else {sensor_temp_outdoor_type_block.classList.add('disabled')}
        sensor_temp_outdoor.onclick = () => {
            if (sensor_temp_outdoor.checked == true) {
                sensor_temp_outdoor_type_block.classList.remove('disabled')
            }
            else {sensor_temp_outdoor_type_block.classList.add('disabled')}
        }
    };

    let coolerFunc = function () {
        let cool_container = document.querySelector('.cool_container');
        let coolType = document.querySelector('.cool_type')
        let coolAlarmBlock = document.querySelector('.cool_alarm_block')
        cool_container.classList.remove('disabled');
        addListeners(['', '', '', '.cool_type', '', ''])
        if (messageData['cool_type'] == 'frion') {
                coolAlarmBlock.classList.remove('disabled')
                addListeners(['', '.cool_checkbox', '', '', '', ''])
        }
         else {coolAlarmBlock.classList.add('disabled')}
        coolType.onclick = () => {
            if (messageData['cool_type'] == 'frion') {
                coolAlarmBlock.classList.remove('disabled')
                addListeners(['', '.cool_checkbox', '', '', '', ''])
            }
            else {coolAlarmBlock.classList.add('disabled')}
        }
    }

    let dehumidsFunc = function() {
        let dehumidContainer = document.querySelector('.dehumids_container')
        dehumidContainer.classList.remove('disabled')
        addListeners(['', '.humid_checkbox', '', '', '', ''])
    }

// Команды кнопок параметры

    let commandsButtons = {
        vents: ventsFunc,
        heaters: heatersFunc,
        coolers: coolerFunc,
        dehumids: dehumidsFunc,
        dampers: dampersFunc,
        filters: filtersFunc,
        reserve: "",
        cabinet: cabinetFunc
    }

// Функция включения кнопок параметры

    let onButton = function(cl) {
        let butts = document.querySelectorAll(cl);
        for (let index = 0; index<butts.length; index++) {
            butts[index].removeAttribute('disabled');
            butts[index].onclick = () => {
                hideParameters();
                if (butts[index].value == "vents" || butts[index].value == "cabinet") {
                    commandsButtons[butts[index].value]();
                }
                else if (messageData[refButtons[butts[index].value]] == 'true') {
                    commandsButtons[butts[index].value]();
                    }
                else if (messageData[refButtons[butts[index].value][0]] == 'true' || messageData[refButtons[butts[index].value][1]] == 'true') {
                    commandsButtons[butts[index].value](messageData[refButtons[butts[index].value][0]], messageData[refButtons[butts[index].value][1]]);
                };
            };
        };
    }

// Функция выключения кнопок

    let offButton = function(cl) {
        let butts = document.querySelectorAll(cl);
        for (let index = 0; index<butts.length; index++) {
            butts[index].setAttribute('disabled', 'disabled');
        };
    }

// Скрыть элементы на главной странице

    let hideElements = function(cl) {
        let elements = document.getElementsByClassName(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 0;";
        };
    };

// Показать  элементы на главной странице

    let showElements = function(cl) {
        let elements = document.getElementsByClassName(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 1;";
        };
    };

// Очистить окно параметров

    let hideParameters = function () {
        let allParameters = document.querySelectorAll(".hide_param");
        for (let index=0; index<allParameters.length; index++) {
            allParameters[index].classList.add('disabled')
        };
    }

    let hideAllImages = function () {
        let allImagesContainer = document.querySelector(".img_container")
        let allImages = document.querySelectorAll('.img_container img')
        if (allImages.length != 0) {
            for (let i = 0; i<allImages.length; i++) {
                allImages[i].style.opacity = '0'
            }
        }
        allImagesContainer.innerHTML = '';

    };

    let showImages = function (lst) {
        let container = document.querySelector(".img_container")
        hideAllImages();
        for (let index=0; index<lst.length; index++) {
            if (lst[index] != '') {
                const imgElement = document.createElement('img');
                imgElement.src = lst[index];
                imgElement.style.opacity = '0'
                container.appendChild(imgElement);
                imgElement.style.opacity = '1'
            };
        };
    };


// обработка выбора типа системы

    for (let radio=0; radio<systemType.length; radio++) {
        systemType[radio].onclick = () => {
            typeSystem = systemType[radio].value
            websocketClient.send(JSON.stringify({"type": systemType[radio].value}));
            for (el in messageData) {messageData[el] = "false"};
            if (typeSystem == 'In_out') {
                messageData['FC_in'] = "FC";
                messageData['FC_out'] = "FC";
            }
            else if (typeSystem == "In") {
                messageData['FC_in'] = "FC";
                messageData['FC_out'] = "NOT_FC";
            }
            else if (typeSystem == "Out") {
                messageData['FC_in'] = "Not_FC";
                messageData['FC_out'] = "FC";
            };
            messageData['shutdown_fire_signal'] = 'true';
            messageData['signal_work'] = 'true';
            messageData['signal_alarm'] = 'true';
            for (el in defaultNumeric) {messageData[el] = defaultNumeric[el]};
            hideParameters();
            hideAllImages();
        };
    };

// Фрэйм для загрузки документов

    specButton.onclick = () => {
        if (typeSystem != null) {
            websocketClient.send(JSON.stringify({'get_exel': 'true'}));
        }
    }

    let getDataDocument = function (file_path=null) {
        let companyName = document.querySelector('#company_name')
        let companyObject = document.querySelector('#company_object')
        let tcpNumber = document.querySelector('#tcp_number')
        let customer = document.querySelector('#customer')
        let executor = document.querySelector('#executor')
        let dataDocument = {
            'name': companyName.value,
            'object': companyObject.value,
            'number': tcpNumber.value,
            'customer': customer.value,
            'executor': executor.value,
            'path': file_path
        };
        return JSON.stringify(dataDocument)
    }

    let exelDownload = function (string, string2, string3, string4) {
        let frame = document.querySelector(".exel_frame")
        frame.style.top = "0"
        let buttSpec = document.querySelector('#spec_button')
        let buttTcp = document.querySelector('#tcp_button')
        let buttPdf = document.querySelector('#pdf_button')
        let buttScheme = document.querySelector('#scheme_button')
        let buttKrest = document.querySelector('#krest')
        buttKrest.onclick = () => {
            frame.style.top = '-550px';
        }
        buttSpec.onclick = () => {
            buttSpec.href = document.URL.split('/')[1] + string + '?data=' + getDataDocument();
        };
        buttTcp.onclick = () => {
          buttTcp.href = document.URL.split('/')[1] + string2 + '?data=' + getDataDocument();
        };
        buttPdf.onclick = () => {
            buttPdf.href = document.URL.split('/')[1] + string3 + '?data=' + getDataDocument();
        }
        buttScheme.onclick = () => {
            buttScheme.href = document.URL.split('/')[1] + 'elscheme' + '?data=' + getDataDocument(string4);
        }
    }

// Вывод сигнало ПЛК

let showSignals = function (signals) {
    let signalsContainer = document.querySelector('.signals')
    let signalsSpan = document.querySelectorAll('.sig_list')
    for (let index=0; index<signals.length; index++) {
        signalsSpan[index].textContent = signals[index];
    }
    signalsContainer.style.opacity = '1';
}

// Вывод цены

let showPrice = function (numPrice) {
    if (String(numPrice).length <= 6) {
        let textPrice = String(numPrice).slice(0, -3) + ' ' + String(numPrice).slice(-3) + ' руб.'
        document.getElementById('price').textContent = textPrice;
    }
    else {
        let textPrice = String(numPrice).slice(0, -6) + ' ' + String(numPrice).slice(-6, -3) + ' ' + String(numPrice).slice(-3) + ' руб.'
        document.getElementById('price').textContent = textPrice;
    }
}


let showModal = function(modal) {
    modal.style.opacity = 1;
     setTimeout(() => modal.style.opacity = 0, 1000)
}

systemId = null

// Сохранение конфигурации
let saveConfig = document.querySelector('#config_button')
saveConfig.onclick = () => {
    let companyName = document.querySelector('#company_name')
    let companyObject = document.querySelector('#company_object')
    let tcpNumber = document.querySelector('#tcp_number')
    let customer = document.querySelector('#customer')
    let executor = document.querySelector('#executor')
    let systemName = document.querySelector('#system_name')
    let modal = document.querySelector('.modal')
    showModal(modal)
    let data = {
        'command': 'save_config',
        'companyName': companyName.value,
        'companyObject': companyObject.value,
        'tcpNumber': tcpNumber.value,
        'customer': customer.value,
        'executor': executor.value,
        'system_name': systemName.value,
        'system_id': systemId
    }
    websocketClient.send(JSON.stringify(data))
}


// Функция установки типа системы
let setSystemType = function(receiveType) {
    if (receiveType['type'] == 'In_out') {
        systemType[0].click();
    }
    else if (receiveType['type'] == 'In') {
        systemType[1].click();
    }
    else if (receiveType['type'] == 'Out') {
        systemType[2].click();
    }
}

// Функция для установки параметров сохранённой системы
let setParameters = function(receiveParam) {
    for (item in receiveParam) {
        if (item == 'select_0') {
            sel = document.querySelectorAll('.select')
            sel[0][1].selected = true
            selectFunc(0, sel[0])
        }
        else if (item == 'select_1') {
            sel = document.querySelectorAll('.select')
            sel[1][1].selected = true
            selectFunc(1, sel[1])
        }
        else if (item == 'filt_in') {
            filt = document.querySelector('#filt_in')
            filt.click()
        }
        else if (item == 'filt_out') {
            filt = document.querySelector('#filt_out')
            filt.click()
        }
        else if (item == 'damp_in') {
            damp = document.querySelector('#damp_in')
            damp.click()
        }
        else if (item == 'damp_out') {
            damp = document.querySelector('#damp_out')
            damp.click()
        }
        else {
            messageData[item] = 'true'
        }
    }
    websocketClient.send(JSON.stringify(messageData))
}

let setNumParameters = function(receiveNumParam) {
    for (item in receiveNumParam) {
        messageData[item] = receiveNumParam[item];
    }
    websocketClient.send(JSON.stringify(messageData))
}


// Получение данных о сохранённой системе

let systemConfig = document.querySelector('#systemConfig')
websocketClient.onopen = () => {
    systemConfig = JSON.parse(systemConfig.value);
    console.log(systemConfig['status'])
    if (systemConfig['status'] != 'default') {
        setSystemType(JSON.parse(systemConfig['sys_type']))
        receiveParam = JSON.parse(systemConfig['param'])
        receiveNumParam = JSON.parse(systemConfig['num_param'])
        receiveName = systemConfig['name']
        receiveObject = systemConfig['object']
        receiveTcp = systemConfig['tcp']
        receiveCustomer = systemConfig['customer']
        receiveExecutor = systemConfig['executor']
        receiveSystemName = systemConfig['system_name']
        receiveSystemId = systemConfig['system_id']
        setTimeout(setParameters, 500, receiveParam)
        setTimeout(setNumParameters, 500, receiveNumParam)
        let companyName = document.querySelector('#company_name')
        let companyObject = document.querySelector('#company_object')
        let tcpNumber = document.querySelector('#tcp_number')
        let customer = document.querySelector('#customer')
        let executor = document.querySelector('#executor')
        let systemName = document.querySelector('#system_name')
        companyName.value = receiveName
        companyObject.value = receiveObject
        tcpNumber.value = receiveTcp
        customer.value = receiveCustomer
        executor.value = receiveExecutor
        systemName.value = receiveSystemName
        systemId = receiveSystemId
    }
    else if(systemConfig['status'] == 'default') {
        console.log('ok')
        receiveName = systemConfig['name']
        receiveObject = systemConfig['object']
        receiveTcp = systemConfig['tcp']
        receiveCustomer = systemConfig['customer']
        receiveExecutor = systemConfig['executor']
        receiveSystemName = systemConfig['system_name']
        receiveSystemId = systemConfig['system_id']
        let companyName = document.querySelector('#company_name')
        let companyObject = document.querySelector('#company_object')
        let tcpNumber = document.querySelector('#tcp_number')
        let customer = document.querySelector('#customer')
        let executor = document.querySelector('#executor')
        let systemName = document.querySelector('#system_name')
        companyName.value = receiveName
        companyObject.value = receiveObject
        tcpNumber.value = receiveTcp
        customer.value = receiveCustomer
        executor.value = receiveExecutor
        systemName.value = receiveSystemName
        systemId = receiveSystemId
        }
    }


// Обработка сообщений

    websocketClient.onmessage = (message) => {
        mes = JSON.parse(message.data);
        showPrice(mes['price']);
        if (mes['type'] == "In_out") {
            showElements('PV');
            showElements('hide_V');
            showElements('hide_P');
            onCheck('.hide_V input');
            onCheck('.hide_P input');
            onSelect();
            offButton(".btn_V");
            onButton(".btn_PV");
        }
        else if (mes['type'] == "In") {
            showElements('P');
            showElements('hide_V');
            onCheck('.hide_V input');
            hideElements('hide_P');
            offCheck('.hide_P input');
            onSelect();
            offButton(".btn_V");
            onButton(".btn_PV");
        }
        else if (mes['type'] == "Out") {
            hideElements('PV');
            showElements('V');
            showElements('hide_P');
            onCheck('.hide_P input')
            hideElements('hide_V');
            offCheck('.hide_V input');
            offSelect();
            offButton(".btn_PV");
            onButton(".btn_V");
        }
        if (mes["href"] != undefined) {
            exelDownload(mes['href'], mes['href2'], mes['href3'], mes['href4'])
        }
        if (mes["img_list"] != undefined) {
            showImages(mes['img_list']);
        }
        showSignals(mes['signals']);
    }

})