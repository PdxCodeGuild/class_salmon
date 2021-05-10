let num1 = document.getElementById("num1")
let num2 = document.getElementById("num2")
let calcBtn = document.getElementById("calc")
let resultsUl = document.getElementById("results")
let clearBtn = document.getElementById("clear")

// function callback(event) {
//     // console.log(event)
//     let result = parseFloat(num1.value) + parseFloat(num2.value)

//     resultsUl.innerText = result
// }

// num1.addEventListener('input', callback)
// num2.addEventListener('input', callback)
// document.body.addEventListener('mousemove', function(event) {
//     console.log(event.x, event.y)
// })

function addCallback(event) {
    // console.log(event)
    let result = parseFloat(num1.value) + parseFloat(num2.value)

    let li = document.createElement('li')
    li.innerText = result

    let btn = document.createElement('button')
    btn.innerText = "-"
    btn.addEventListener('click', function() {
        btn.parentElement.remove()
    })

    li.appendChild(btn)
    resultsUl.appendChild(li)
}

calcBtn.addEventListener('click', addCallback)
num1.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addCallback()
    }
})
num2.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addCallback()
    }
})

// calcBtn.addEventListener('click', function(event) {
//     // console.log(event)
//     let result = parseFloat(num1.value) + parseFloat(num2.value)

//     let li = document.createElement('li')
//     li.innerText = result

//     let btn = document.createElement('button')
//     btn.innerText = "-"
//     btn.addEventListener('click', function() {
//         btn.parentElement.remove()
//     })

//     li.appendChild(btn)
//     resultsUl.appendChild(li)
// })

clearBtn.addEventListener('click', function() {
    resultsUl.innerHTML = ""
})


////////////////////////////////////////////////


let numsDiv = document.getElementById("nums")
let addBtn = document.getElementById("add-num")
let avgBtn = document.getElementById("calc-avg")
let avgResults = document.getElementById("average")
let controls = document.getElementById('controls')

let numbers = document.getElementsByClassName("nums")

avgBtn.addEventListener('click', function() {
    let sum = 0
    for (let i = 0; i < numbers.length; i++) {
        sum += parseFloat(numbers[i].value)
    }
    let result = sum / numbers.length
    avgResults.innerText = result
})

addBtn.addEventListener('click', function() {
    let newInput = document.createElement('input')
    newInput.type = 'number'
    newInput.classList.add('nums')
    numsDiv.appendChild(newInput)

    if (numbers.length <= 3) {
        let removeBtn = document.createElement('button')
        removeBtn.innerText = '-'
        removeBtn.addEventListener('click', function() {
            numsDiv.lastElementChild.remove()
            if (numbers.length < 3) {
                removeBtn.remove()
            }
        })
        controls.appendChild(removeBtn)
    }
})


//////////////////////////////////////////////////////////


let timingBtns = document.getElementsByClassName('btn')
let stopDiv = document.getElementById('stop')

for (let i=0; i < timingBtns.length; i++) {
    timingBtns[i].addEventListener('click', function() {
        let interval = setInterval(function() {
            console.log(i)
        }, i*1000)

        let btn = document.createElement('button')
        btn.innerText = `Cancel ${i}`
        btn.addEventListener('click', function() {
            clearInterval(interval)
            this.remove()
        })
        stopDiv.appendChild(btn)
    })
}