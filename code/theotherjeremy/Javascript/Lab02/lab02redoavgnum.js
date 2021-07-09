let nums = []
let addup = (prompt('Enter a number to add to the list. Enter "done" to exit.'))
while (true){
    if (addup === 'done') {
        break
    } else {
        nums.push(addup)
        addup = prompt(
            'Enter a number to add to the list.\nEnter "done" to exit.  ')
        }}

let nums2 = 0
for (num of nums) {
    nums2 = nums2 + parseFloat(num)
}

let final = ((nums2)) / ((nums.length))
alert(`You entered ${nums2} The average of these numbers is ${final}.`)
