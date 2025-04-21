let addTcpButt = document.querySelector('#config_button')
let projectFrame = document.querySelector('.project_frame')
let krestButt = document.querySelector('#krest')
let updateButts = document.querySelector('.update_button')
let inputQuant = document.querySelectorAll('.input_quant')
let sysId = document.querySelectorAll('.system_id')
let tcpNumber = document.querySelector('#tcp_number')
let tcpId = document.querySelector('#tcp_id')
let targetUrl = document.URL.split('/')[0] + '//' + document.URL.split('/')[2] + '/systems_update'


let hideFrame = function () {
    projectFrame.style.opacity = '0';
    projectFrame.style.pointerEvents = 'none';
}

addTcpButt.addEventListener('click', function() {
    projectFrame.style.opacity = '1';
    projectFrame.style.pointerEvents = 'unset';
})

krestButt.addEventListener('click', hideFrame)

let sendArray = []

for (let j=0; j<inputQuant.length; j++) {
    inputQuant[j].addEventListener('change', function() {
        updateButts.style.opacity = '1';
        updateButts.style.pointerEvents = 'unset';
        sendArray.push(j)
    });
}
updateButts.addEventListener('click', function() {
    var uniqIdS = new Set(sendArray)
    sendArray = Array.from(uniqIdS)
    var systems_data = {}
    for (i in sendArray) {
        systems_data[sysId[sendArray[i]].innerHTML] = inputQuant[sendArray[i]].value
    }
    systems_data = JSON.stringify(systems_data)
    var params = new URLSearchParams('tcp_id='+tcpId.innerHTML + '&tcp_number='+tcpNumber.innerHTML + '&systems='+systems_data)
    fetch(targetUrl+'?'+params, {
        method: 'POST',
        headers: {
            'Content-type': 'application/x-www-form-urlencoded'
        },
    })
    updateButts.style.opacity = '0';
    updateButts.style.pointerEvents = 'none';
});
