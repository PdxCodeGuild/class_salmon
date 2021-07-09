// def validate(cc_num):
//     cc_num = list(cc_num)
//     cc_num = [int(index) for index in cc_num]   
//     check_digit = cc_num.pop(-1)
//     cc_num.reverse()
//     cc_num = [cc_num[index] * 2 if index % 2 == 0 else cc_num[index] for index in range(len(cc_num))]
//     cc_num = [cc_num[index] - 9 if cc_num[index] > 9 else cc_num[index] for index in range(len(cc_num))]
//     total = sum(cc_num)
//     if total % 10 == check_digit:
//         return True
//     else:
//         return False
     
// cc_num = input('Enter Credit Card Number: ')
// output = 'Card Number Valid!' if validate(cc_num) is True else 'Invalid Card Number! '
// print(output)
// 4556737586899855
let cc_num = ''
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
cc_num = prompt("Enter Credit Card Number: ")
// console.log(validate(cc_num))
let b = validate(cc_num);
console.log(b)
if (!b) {
    alert("Credit Card invalid!")
} else {
   alert("Credit Card valid!")
}
// console.log(output)