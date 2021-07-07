let dd1 = document.querySelector('#dd1');
let dd2 = document.querySelector('#dd2');
let result = document.querySelector('#result');


let btnFinal = document.querySelector('#btnFinal')
let units = ['feet', 'miles', 'meters', 'kilometers', 'yards', 'inches']


// for (let i=0; i<units.length; ++i) {
//     let option = document.createElement('option')
//     option.innerText = units[i]
//     option.value = units[i]
//     dd1.appendChild(option)
// }

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
    let meters = userDist * (convDict[dd1])
    console.log(meters)
    console.log((userDist).value)
    console.log((dd2).value)
    console.log((dd1).value)
    // result.innerText = userDist + dd1 + "  =  "  + output + dd2 
    result.innerText = 'hello'    
})
