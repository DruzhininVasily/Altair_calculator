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
        res_out: "false"
    }

    let refButtons = {
        heaters: "select_0",
        coolers: "select_1",
        humids: "select_2",
        dampers: ["damp_in", 'damp_out'],
        filters: ["filt_in", "filt_out"],
        reserve: ["res_in", "res_out"]
    }

    let price = document.querySelector("#price");
    let systemType = document.querySelectorAll(".radio input")

    let websocketClient  = new WebSocket("ws://127.0.0.1:5000");

    let selectFunc = function (index, e) {
        selIndex = {0: "select_0", 1: "select_1", 2: "select_2"}
        messageData[selIndex[index]] = e.target.value
        websocketClient.send(JSON.stringify(messageData));
    };

    let onSelect = function () {
        let sel = document.querySelectorAll(".select");
        for (let i=0; i<sel.length; i++) {
            sel[i].removeAttribute('disabled');
            sel[i].selectedIndex = 0;
            sel[i].addEventListener('change', () => selectFunc(i, event))
        };
    };

    let offSelect = function () {
        let sel = document.querySelectorAll(".select");
        for (let i=0; i<sel.length; i++) {
            sel[i].selectedIndex = 0;
            sel[i].setAttribute('disabled', 'disabled')
        };
    };

    let onCheck = function(cl) {
        let elements = document.querySelectorAll(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 1;";
            elements[index].removeAttribute('disabled');
            elements[index].checked = false;
            elements[index].onclick = () => {
                messageData[elements[index].id] = String(elements[index].checked)
                websocketClient.send(JSON.stringify(messageData));
            }
        };
    };

    let offCheck = function(cl) {
        let elements = document.querySelectorAll(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 0;";
            elements[index].setAttribute('disabled', 'disabled');
        };
    };


    let ventsFunc = function() {
        console.log("ventil");
    };

    let commandsButtons = {
        vents: ventsFunc,
        heaters: "",
        coolers: "",
        humids: "",
        dampers: "",
        filters: "",
        reserve: "",
        cabinet: ""
    }

    let onButton = function(cl) {
        let butts = document.querySelectorAll(cl);
        for (let index = 0; index<butts.length; index++) {
            butts[index].removeAttribute('disabled');
            butts[index].onclick = () => {
                if (butts[index].value == "vents" || butts[index].value == "cabinet") {
                    console.log("ventelyator");
                    commandsButtons[butts[index].value]();
                }
                else if (messageData[refButtons[butts[index].value]] == 'true') {
                    console.log(butts[index].value);
                    }
                else if (messageData[refButtons[butts[index].value][0]] == 'true' || messageData[refButtons[butts[index].value][1]] == 'true') {
                    console.log(butts[index].value);
                };
            };
        };
    }

    let offButton = function(cl) {
        let butts = document.querySelectorAll(cl);
        for (let index = 0; index<butts.length; index++) {
            butts[index].setAttribute('disabled', 'disabled');
        };
    }

    let hideElements = function(cl) {
        let elements = document.getElementsByClassName(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 0;";
        };
    };

    let showElements = function(cl) {
        let elements = document.getElementsByClassName(cl);
        for (let index = 0; index<elements.length; index++) {
            elements[index].style = "opacity: 1;";
        };
    };

    for (let radio=0; radio<systemType.length; radio++) {
        systemType[radio].onclick = () => {
            typeSystem = systemType[radio].value
            websocketClient.send(JSON.stringify({"type": systemType[radio].value}));
            for (el in messageData) {messageData[el] = "false"};
        };
    };


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
            offButton(".btn_V")
            onButton(".btn_PV")
        }
        else if (mes['type'] == "In") {
            showElements('P');
            showElements('hide_V');
            onCheck('.hide_V input');
            hideElements('hide_P');
            offCheck('.hide_P input');
            onSelect();
            offButton(".btn_V")
            onButton(".btn_PV")
        }
        else if (mes['type'] == "Out") {
            hideElements('PV');
            showElements('V');
            showElements('hide_P');
            onCheck('.hide_P input')
            hideElements('hide_V');
            offCheck('.hide_V input');
            offSelect();
            offButton(".btn_PV")
            onButton(".btn_V")
        }
    }
})