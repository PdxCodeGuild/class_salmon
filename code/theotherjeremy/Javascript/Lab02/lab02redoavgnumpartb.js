let numInput = document.getElementById('num')
let numList = []

let output_div = document.querySelector('#output_div');
let output_div2 = document.querySelector('#output_div2');
addIt.onclick = function() {
    console.log(numInput.value)    
    numList.push(+numInput.value)
    output_div.innerText = numList 


}

// while (true){
//     if (addup === 'done') {
//         break
//     } else {
//         nums.push(addup)
//         addup = prompt(
//             'Enter a number to add to the list.\nEnter "done" to exit.  ')
//         }}

let nums2 = 0

final.onclick = function(evt) {
    for (num of numList) {
        nums2 = nums2 + parseFloat(num)}
    let final = ((nums2)) / ((numList.length))
    output_div.innerText = `The average of those ${numList.length} numbers is ${final}.`



}
   
