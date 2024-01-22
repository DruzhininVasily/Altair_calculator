document.addEventListener('DOMContentLoaded', function(){
    let messageData = {
        select_0: "No",
        select_1: "No",
        select_2: "No"
    }

    let price = document.querySelector("#price");
    let systemType = document.querySelectorAll(".radio input")

    let websocketClient  = new WebSocket("ws://127.0.0.1:5000");

    let selectFunc = function (index, e) {
        selIndex = {0: "select_0", 1: "select_1", 2: "select_2"}
        messageData[selIndex[index]] = e.target.value
        websocketClient.send(JSON.stringify(messageData));
        console.log(e.target.value)
    }

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
            websocketClient.send(JSON.stringify({"type": systemType[radio].value}));
            for (el in messageData) {messageData[el] = "No"};
        };
    };


    websocketClient.onmessage = (message) => {
        mes = JSON.parse(message.data)
        if (mes['type'] == "In_out") {
            document.getElementById('price').textContent = '300000руб';
            showElements('PV');
            showElements('hide_V');
            showElements('hide_P');
            onSelect();
        }
        else if (mes['type'] == "In") {
            document.getElementById('price').textContent = '200000руб';
            showElements('P');
            showElements('hide_V');
            hideElements('hide_P');
            onSelect();
        }
        else if (mes['type'] == "Out") {
            document.getElementById('price').textContent = '100000руб';
            hideElements('PV');
            showElements('V');
            showElements('hide_P');
            hideElements('hide_V');
            offSelect();
        }
    }
})