// let cc_num = ''
function validate(cc_num) {
    cc_num = Array.from(cc_num);
    // console.log(cc_num)
    let num_list1 = [];
    let num_list2 = [];
    for (num of cc_num) {
        let int = parseFloat(num);
        num_list1.push(int);
        num_list2.push(int);
    }
    // console.log(num_list1)
    let check_digit = num_list1.pop()
    // console.log(check_digit)
    // console.log(num_list1)
    num_list1.reverse();
    // console.log(num_list1)
    let i = 0;
    while (i < num_list1.length) {
        if (i % 2 === 0) {
            num_list1[i] *= 2;
        }
        i++
    }
    // console.log(num_list1)
    i = 0;
    while (i < num_list1.length) {
        // console.log(num)
        if (num_list1[i] > 9) {
            num_list1[i] -= 9;
        }
        i++
    }
    // console.log(num_list1)
    let total = 0;
    for (num of num_list1) {
        total += num
    }
    // console.log(total)
    if (total % 10 === check_digit) {
        return true
    }
    else {
        return false
    }

}
// cc_num = prompt("Enter Credit Card Number: ")
// console.log(validate(cc_num))

let body = document.getElementById('body')

let form = document.createElement('form');
    form.action = '';
    form.method = "post";

body.appendChild(form)

let card_num = document.createElement("input");
    card_num.type = "text";
    card_num.id = "card-number";

form.appendChild(card_num)

let submit_btn = document.createElement('input');
    submit_btn.type = "submit";
    submit_btn.value = "Valitate"

form.appendChild(submit_btn)
// console.log(submit_btn)

let output = document.createElement('h4');
    output.id = "result"
    output.innerText = ""

body.appendChild(output);

submit_btn.addEventListener("click", function(event){
    event.preventDefault();
    let input = document.getElementById("card-number");
    let cc_num = input.value
    console.log(cc_num)
    validate(cc_num);
    let b = validate(cc_num);
    console.log(b)
    if (!b) {
    // alert("Credit Card invalid!")
        output.innerText = "Credit Card invalid!"

    } else {
//    alert("Credit Card valid!")
        output.innerText = "Credit Card valid!"
    }

})


