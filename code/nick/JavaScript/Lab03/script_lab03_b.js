let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

// console.log(data)
function peaks(data) {
    let peak_indices = []
    for (let i=0; i<data.length; ++i) {
        if ( i === 0 || i === ((data.length)-1)) {
            // console.log("firstloop")
            continue
        }
        // #won't let me start on the list at 0 or -1 position; added above if statement
        else if (data[i-1] < data[i] && data[i] > data[i+1]) {
            // console.log(".")
            peak_indices.push(i)
        }
        else if (data[i-1] > data[i] && data[i] < data[i+1]) {
            continue
        }
    }
    return peak_indices //make sure the return is outside of the for loop!!
}

let peak_indices = peaks(data)


function valleys(data) {
    let valleys_indices = []
    for (let i=0; i < data.length; ++i) {
        if (i === 0 || i === ((data.length)-1)) { //gave me "length is not a function" error
            continue
        } else if (data[i-1] > data[i] && data[i] < data[i+1]) {
            valleys_indices.push(i)
        } else if (data[i-1] < data[i] && data[i] > data[i+1]) {
            continue
        }
    }
    return valleys_indices //make sure the return is outside of the for loop!!
}
let valley_indices = valleys(data)

function peaks_and_valleys(peak_indices, valley_indices) { //referenced https://stackoverflow.com/questions/4856717/javascript-equivalent-of-pythons-zip-function
    let zip_peaks_and_valleys = rows => rows[0].map((_,c) => rows.map(row => row[c]))
    const peaks_valleysZipped = zip_peaks_and_valleys([peak_indices, valley_indices])
    return peaks_valleysZipped
}
console.log(peaks_and_valleys(peak_indices,valley_indices))
let result = peaks_and_valleys(peak_indices, valley_indices)
alert(result)