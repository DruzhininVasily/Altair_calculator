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
        voltage_vent_in: "false",
        voltage_vent_out: "false",
        FC_in: "false",
        FC_out: "false",
        dif_in: "false",
        dif_out: "false",
        vent_power_in: "0",
        vent_power_out: "0",
        first_heater_type: "false",
        first_pump: "false",
        first_signal: "false",
        first_sensor: "false",
        first_thermostat: "false",
        first_pump_voltage: "false",
        first_valve_voltage: "false",
        first_confirm: "false",
        first_steps: "0",
        electrical_first_step_power: "0",
        electrical_first_step_signal: "false",
        first_electrical_thermal: "0",
        second_heat_choice: "false",
        second_heat_type: "false",
        second_pump: "false",
        second_signal: "false",
        second_sensor: "false",
        second_thermostat: "false",
        second_pump_voltage: "false",
        second_valve_voltage: "false",
        second_confirm: "false",
        second_steps: "0",
        electrical_second_step_power: "0",
        electrical_second_step_signal: "false",
        second_electrical_thermal: "0",
        in_damper_voltage: 'false',
        in_damper_confirm: 'false',
        in_damper_heat: 'false',
        in_damper_heat_voltage: 'false',
        in_damper_heat_power: '0',
        out_damper_voltage: 'false',
        out_damper_confirm: 'false',
        out_damper_heat: 'false',
        out_damper_heat_voltage: 'false',
        out_damper_heat_power: '0',
        in_filter_quantity: '0',
        out_filter_quantity: '0',
        switch_type: 'false',
        base_controller: '0',
        shutdown_fire_signal: 'false',
        sensor_temp_outdoor: 'false',
        sensor_temp_indoor: 'false',
        sensor_humid: 'false',
        sensor_hood: 'false',
        signal_work: 'false',
        signal_alarm: 'false',
        work_on_sched: 'false',
        remote_control: 'false'
    }

    let refButtons = {
        heaters: "select_0",
        coolers: "select_1",
        humids: "select_2",
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
        first_confirm: 'false',
        electrical_first_step_signal: 'false',
        second_heat_choice: 'false',
        };

    let heaterSecondBoolDefault = {
        second_heat_type: 'false',
        second_pump: 'true',
        second_signal: 'true',
        second_sensor: 'false',
        second_thermostat: 'false',
        second_pump_voltage: 'false',
        second_valve_voltage: 'false',
        second_confirm: 'false',
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
        in_damper_confirm: 'false',
        in_damper_heat: 'false',
        in_damper_heat_voltage: 'false',
        in_damper_heat_power: '0'
    };

    let dampOutDefault = {
        out_damper_voltage: 'false',
        out_damper_confirm: 'false',
        out_damper_heat: 'false',
        out_damper_heat_voltage: 'false',
        out_damper_heat_power: '0'
    }

    let = powerData = {0: "0.18", 1: "0.22", 2: "0.55", 3: "1.5", 4: "2.2", 5: "4", 6: "5.5", 7: "7.5", 8: "11", 9: "15", 10: "22", 11: "30", 12: "55"}
    let = powerDamperHeatData = {0: "0.1", 1: "0.2", 2: "0.3", 3: "0.4", 4: "0.5", 5: "0.6", 6: "0.7", 7: "0.8", 8: "0.9", 9: "1.0", 10: "1.1", 11: "1.2"}

    let price = document.querySelector("#price");
    let systemType = document.querySelectorAll(".radio input")

    let websocketClient  = new WebSocket("ws://127.0.0.1:5000");

// Функция для обработки input type="select" на основном экране

    let selectFunc = function (index, e) {
        selIndex = {0: "select_0", 1: "select_1", 2: "select_2"}
        messageData[selIndex[index]] = e.target.value
        if (e.target.value == 'false') {
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
            if (e.target.checked == true) {
                DamperHeatContainer.classList.remove('disabled')
                addListeners(['', '', damperRange, damperSelect], damperSpan, powerDamperHeatData)
                messageData[e.target.name] = 'true';
                websocketClient.send(JSON.stringify(messageData));
            }
            else if (e.target.checked == false) {
                DamperHeatContainer.classList.add('disabled');
                document.getElementById(dampHeatPower).value = '0';
                document.getElementById(dampHeatVoltage).value = 'false';
                messageData[dampHeatPower] = '0';
                messageData[dampHeatVoltage] = 'false';
                messageData[e.target.name] = 'false';
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
                                        document.getElementsByClassName(el)[0].value = 'false'
                                    };
                                };
                                addListeners(['', '.in_damper_checkbox', '', '.in_damper_select', '', '']);
                                let inDamperHeatChoice = document.querySelector('.in_damper_heat')
                                inDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.in_damper_heat_parameter_container', '.in_damper_heat_range', '.in_damper_heat_select', '#in_damper_heat_power_span', 'in_damper_heat_power', 'in_damper_heat_voltage'));
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
                                        document.getElementsByClassName(el)[0].value = 'false'
                                    };
                                };
                                addListeners(['', '.out_damper_checkbox', '', '.out_damper_select', '', '']);
                                let outDamperHeatChoice = document.querySelector('.out_damper_heat');
                                outDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.out_damper_heat_parameter_container', '.out_damper_heat_range', '.out_damper_heat_select', '#out_damper_heat_power_span', 'out_damper_heat_power', 'out_damper_heat_voltage'));
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
            }}
            else {
                if (messageData[radioObjects[index].name] == "true")
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
        let paramVent_in = document.querySelector(".paramVent_in")
        let paramVent_out = document.querySelector(".paramVent_out")
        if (typeSystem == "In_out") {
            paramVent_in.classList.remove('disabled');
            paramVent_out.classList.remove('disabled');
            addListeners(['.vent_radio_info_in', '.vent_check_info_in', '.vent_range_info_in', ''], "#pow_span_in", powerData);
            addListeners(['.vent_radio_info_out', '.vent_check_info_out', '.vent_range_info_out', ''], "#pow_span_out", powerData)
        }
        else if (typeSystem == "In") {
            paramVent_in.classList.remove('disabled');
            paramVent_out.className = ("paramVent_out hide_param disabled");
            addListeners(['.vent_radio_info_in', '.vent_check_info_in', '.vent_range_info_in', ''], "#pow_span_in", powerData);
        }
        else if (typeSystem == "Out") {
            paramVent_out.classList.remove('disabled');
            paramVent_in.className = ("paramVent_in hide_param disabled");
            addListeners(['.vent_radio_info_out', '.vent_check_info_out', '.vent_range_info_out', ''], "#pow_span_out", powerData)
        };
    };

// Функция выбора типа нагревателя

    let typeHeatChoice = function (e, elClass, waterClass, list_water, list_elect) {
        let electricalContainer = document.querySelector(elClass);
        let waterContainer = document.querySelector(waterClass);
        if (e.target.value == "true") {
                electricalContainer.classList.remove('disabled');
                waterContainer.classList.add('disabled');
                sendData(e.target.name, e.target.value);
                addListeners([list_elect[0], list_elect[1], list_elect[2], list_elect[3]], list_elect[4], list_elect[5]);
        }
        else {
                electricalContainer.classList.add('disabled');
                waterContainer.classList.remove('disabled');
                addListeners([list_water[0], list_water[1], list_water[2], list_water[3]], list_water[4], list_water[5])
                sendData(e.target.name, e.target.value);
        };
    }


// Функция для обработки окна нагреватели

    let heatersFunc = function () {
        let heatContainer = document.querySelector(".heat_container");
        let secondChoice = document.querySelector(".second_heat_choice");
        let firstTypeHeatChoice = document.querySelector('.heater_type_first')
        heatContainer.classList.remove('disabled');
        addListeners(['', '.first_water_checkbox', '', '.first_water_select'], '', '')
        firstTypeHeatChoice.addEventListener('change', () => typeHeatChoice(event, '.electrical_first_container', '.water_first_container', ['', '.first_water_checkbox', '', '.first_water_select', '', ''], ['', '.first_electrical_checkbox', '.first_electrical_range', '.first_electrical_select', '#first_step_pow_span', powerData]));
        secondChoice.onclick = () => {
            sendData(secondChoice.name, String(secondChoice.checked));
            let secondContainer = document.querySelector(".second_container");
            if (secondChoice.checked == true) {
            secondContainer.classList.remove('disabled');
            addListeners(['', '.second_water_checkbox', '', '.second_water_select'], '', '')
            let secondTypeHeatChoice = document.querySelector(".heater_type_second");
            secondTypeHeatChoice.addEventListener('change', () => typeHeatChoice(event, '.electrical_second_container', '.water_second_container', ['', '.second_water_checkbox', '', '.second_water_select', '', ''], ['', '.second_electrical_checkbox', '.second_electrical_range', '.second_electrical_select', '#second_step_pow_span', powerData]));
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
            inDamperContainer.classList.remove('disabled');
            addListeners(['', '.in_damper_checkbox', '', '.in_damper_select', '', ''])
            let inDamperHeatChoice = document.querySelector('.in_damper_heat')
            inDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.in_damper_heat_parameter_container', '.in_damper_heat_range', '.in_damper_heat_select', '#in_damper_heat_power_span', 'in_damper_heat_power', 'in_damper_heat_voltage'));
        }
        else if (checkIn == 'false') {
            let inDamperContainer = document.querySelector('.in_damper_container');
            inDamperContainer.classList.add('disabled');
        };
        if (checkOut == 'true') {
            let outDamperContainer = document.querySelector('.out_damper_container');
            outDamperContainer.classList.remove('disabled');
            addListeners(['', '.out_damper_checkbox', '', '.out_damper_select', '', '']);
            let outDamperHeatChoice = document.querySelector('.out_damper_heat')
            outDamperHeatChoice.addEventListener('click', () => DampersHeatChoice(event, '.out_damper_heat_parameter_container', '.out_damper_heat_range', '.out_damper_heat_select', '#out_damper_heat_power_span', 'out_damper_heat_power', 'out_damper_heat_voltage'));
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
    };

    let cabinetFunc = function () {
        hideParameters();
        let cabinetContainer = document.querySelector('.cabinet_container');
        cabinetContainer.classList.remove('disabled');
        addListeners(['', '.cabinet_checkbox', '', '.cabinet_select', '', '']);
    };

// Команды кнопок параметры

    let commandsButtons = {
        vents: ventsFunc,
        heaters: heatersFunc,
        coolers: "",
        humids: "",
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

// обработка выбора типа системы

    for (let radio=0; radio<systemType.length; radio++) {
        systemType[radio].onclick = () => {
            typeSystem = systemType[radio].value
            websocketClient.send(JSON.stringify({"type": systemType[radio].value}));
            for (el in messageData) {messageData[el] = "false"};
            messageData['vent_power_in'] = "0";
            messageData['vent_power_out'] = "0";
            messageData['first_steps'] = "0";
            messageData['electrical_first_step_power'] = "0";
            messageData['first_electrical_thermal'] = "0";
            messageData['second_steps'] = "0";
            messageData['electrical_second_step_power'] = "0";
            messageData['second_electrical_thermal'] = "0";
            messageData['in_damper_heat_power'] = "0";
            messageData['out_damper_heat_power'] = "0";
            messageData['in_filter_quantity'] = "0";
            messageData['out_filter_quantity'] = "0";
            messageData['base_controller'] = "0";
            hideParameters();
        };
    };

// Обработка сообщений

    websocketClient.onmessage = (message) => {
        mes = JSON.parse(message.data);
        document.getElementById('price').textContent = mes['price'];
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
            onButton(".btn_PV");;
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
    }
})