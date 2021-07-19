let addNumBtn = document.getElementById("add-num")
let submitBtn = document.getElementById("submitBtn")
let results = document.getElementById("results")

// this builds a list of numbers
var list_nums = []//global scope
addNumBtn.addEventListener("click", function(event) {
    event.preventDefault()
    let nums = document.getElementById("num").value
    console.log(nums)
    function isNumeric(nums) {
        return !isNaN(parseFloat(nums))
    }    
    console.log(isNumeric(nums))
    if (isNumeric(nums) === true) {  //This is supposed to mean is not not a number for the parsefloat of the input https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN
        list_nums.push(parseFloat(nums)) //needs type conversion for the string inputs
        console.log(list_nums)
        let advice = document.createElement("p")
        results.append(advice, String("The number(s) " + String(list_nums) + " has/have been added to the list."))
        console.log(list_nums)
        // return list_nums
    } else {
        let advice = document.createElement("p")
        results.append(advice, String("This is not a number: " + String(nums)))//This does not interrupt the list construction.
        return list_nums
    }
    }
)
submitBtn.addEventListener("click", function(event) {
    event.preventDefault()
    function peaks(list_nums) {
        let peak_indices = []
        for (let i=0; i<list_nums.length; ++i) {
            if ( i === 0 || i === ((list_nums.length)-1)) {
                // console.log("firstloop")
                continue
            }
            // #won't let me start on the list at 0 or -1 position; added above if statement
            else if (list_nums[i-1] < list_nums[i] && list_nums[i] > list_nums[i+1]) {
                // console.log(".")
                peak_indices.push(i)
            }
            else if (list_nums[i-1] > list_nums[i] && list_nums[i] < list_nums[i+1]) {
                continue
            }
        }
        return peak_indices //make sure the return is outside of the for loop!!
    }    
    let peak_indices = peaks(list_nums)       
    function valleys(list_nums) {
        let valleys_indices = []
        for (let i=0; i < list_nums.length; ++i) {
            if (i === 0 || i === ((list_nums.length)-1)) { //gave me "length is not a function" error
                continue
            } else if (list_nums[i-1] > list_nums[i] && list_nums[i] < list_nums[i+1]) {
                valleys_indices.push(i)
            } else if (list_nums[i-1] < list_nums[i] && list_nums[i] > list_nums[i+1]) {
                continue
            }
        }
        return valleys_indices //make sure the return is outside of the for loop!!
    }
    let valley_indices = valleys(list_nums)
    
    function peaks_and_valleys(peak_indices, valley_indices) { //referenced https://stackoverflow.com/questions/4856717/javascript-equivalent-of-pythons-zip-function
        let zip_peaks_and_valleys = rows => rows[0].map((_,c) => rows.map(row => row[c]))
        const peaks_valleysZipped = zip_peaks_and_valleys([peak_indices, valley_indices])
        return peaks_valleysZipped
    }
    console.log(peaks_and_valleys(peak_indices,valley_indices))
    let locations = peaks_and_valleys(peak_indices, valley_indices)
    let advice = document.createElement("p")
    results.append(advice, String("The peaks and valleys of this list appear in order at index locations: " + String(locations)))
})
// console.log(data)
// function peaks(data) {
//     let peak_indices = []
//     for (let i=0; i<data.length; ++i) {
//         if ( i === 0 || i === ((data.length)-1)) {
//             // console.log("firstloop")
//             continue
//         }
//         // #won't let me start on the list at 0 or -1 position; added above if statement
//         else if (data[i-1] < data[i] && data[i] > data[i+1]) {
//             // console.log(".")
//             peak_indices.push(i)
//         }
//         else if (data[i-1] > data[i] && data[i] < data[i+1]) {
//             continue
//         }
//     }
//     return peak_indices //make sure the return is outside of the for loop!!
// }

// let peak_indices = peaks(data)


// function valleys(data) {
//     let valleys_indices = []
//     for (let i=0; i < data.length; ++i) {
//         if (i === 0 || i === ((data.length)-1)) { //gave me "length is not a function" error
//             continue
//         } else if (data[i-1] > data[i] && data[i] < data[i+1]) {
//             valleys_indices.push(i)
//         } else if (data[i-1] < data[i] && data[i] > data[i+1]) {
//             continue
//         }
//     }
//     return valleys_indices //make sure the return is outside of the for loop!!
// }
// let valley_indices = valleys(data)

// function peaks_and_valleys(peak_indices, valley_indices) { //referenced https://stackoverflow.com/questions/4856717/javascript-equivalent-of-pythons-zip-function
//     let zip_peaks_and_valleys = rows => rows[0].map((_,c) => rows.map(row => row[c]))
//     const peaks_valleysZipped = zip_peaks_and_valleys([peak_indices, valley_indices])
//     return peaks_valleysZipped
// }
// console.log(peaks_and_valleys(peak_indices,valley_indices))
// let result = peaks_and_valleys(peak_indices, valley_indices)
// alert(result)