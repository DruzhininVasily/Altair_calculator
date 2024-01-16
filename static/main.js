document.addEventListener('DOMContentLoaded', function(){
    let price = document.querySelector("#price");
    let systemType = document.querySelectorAll(".radio input")

    let websocketClient  = new WebSocket("ws://127.0.0.1:5000");


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
            websocketClient.send(systemType[radio].value)
        };
    };

    websocketClient.onmessage = (message) => {
        if (message.data == "In_out") {
            document.getElementById('price').textContent = '300000руб';
            showElements('PV');
            showElements('hide_V');
            showElements('hide_P');
        }
        else if (message.data == "In") {
            document.getElementById('price').textContent = '200000руб';
            showElements('P');
            showElements('hide_V');
            hideElements('hide_P');
        }
        else if (message.data == "Out") {
            document.getElementById('price').textContent = '100000руб';
            hideElements('PV');
            showElements('V');
            showElements('hide_P');
            hideElements('hide_V');
        }
    }
})