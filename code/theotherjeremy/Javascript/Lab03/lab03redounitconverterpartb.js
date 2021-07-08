let dd1 = document.querySelector('#dd1');
let dd2 = document.querySelector('#dd2');
let result = document.querySelector('#result');


let btnFinal = document.querySelector('#btnFinal')
let units = ['feet', 'miles', 'meters', 'kilometers', 'yards', 'inches']

const convDict = {'meters': 1,
'feet': .3048,
'miles': 1609.34,
'kilometers': 1000,
'inches': .0254,
'yards': .9144}


let finalDict = {'meters': 1,
'feet': 1/.3048,
'miles': 1/1609.34,
'kilometers': 1/1000,
'inches': 1/.0254,
'yards': 1/.9144}

    
btnFinal.addEventListener("click", function(event) {
    event.preventDefault()
    let userDist = document.querySelector('#userDist')
    let meters = userDist.value * (convDict[dd1.value])
    let endResult = meters * (finalDict[dd2.value])
    result.innerText = userDist.value + " " + dd1.value + "  =  " + endResult + ' ' + dd2.value 
     
})
