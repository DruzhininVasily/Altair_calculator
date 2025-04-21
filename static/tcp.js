let addTcpButt = document.querySelector('#config_button')
let projectFrame = document.querySelector('.project_frame')
let krestButt = document.querySelector('#krest')
let hideStatus = document.querySelectorAll('.hide_status')
let selectStatus = document.querySelectorAll('.status_select')
let updateButton = document.querySelector('.update_button')
let tcpIds = document.querySelectorAll('.sys_id')
let targetUrl = document.URL.split('/')[0] + '//' + document.URL.split('/')[2] + '/tcps_update'


let sendArray = []

for (let i=0; i<selectStatus.length; i++) {
    selectStatus[i].options.selectedIndex = hideStatus[i].innerHTML
    selectStatus[i].addEventListener('change', function(){
        updateButton.style.opacity = '1'
        updateButton.style.pointerEvents = 'unset'
        sendArray.push(i)
    })
}


let hideFrame = function () {
    projectFrame.style.opacity = '0';
    projectFrame.style.pointerEvents = 'none';
}

addTcpButt.addEventListener('click', function() {
    projectFrame.style.opacity = '1';
    projectFrame.style.pointerEvents = 'unset';
})

krestButt.addEventListener('click', hideFrame)


updateButton.addEventListener('click', function() {
    var uniqIdS = new Set(sendArray)
    sendArray = Array.from(uniqIdS)
    var tcps_data = {}
    for (i in sendArray) {
        tcps_data[tcpIds[sendArray[i]].innerHTML] = selectStatus[sendArray[i]].options.selectedIndex
    }
    tcps_data = JSON.stringify(tcps_data)
    var params = new URLSearchParams('tcps='+tcps_data)
    fetch(targetUrl+'?'+params, {
        method: 'POST',
        headers: {
            'Content-type': 'application/x-www-form-urlencoded'
        },
    })
    updateButton.style.opacity = '0';
    updateButton.style.pointerEvents = 'none';
})