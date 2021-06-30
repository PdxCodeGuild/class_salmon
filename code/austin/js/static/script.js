/* from random import randint
def pic_6():
    numbers=[randint(1,99) for num in range(6)]
    return(numbers)
def num_matches():
    winning_nums=pic_6()
    entry_nums=pic_6()
    matches=0
    for i in range(6):
        if winning_nums[i] == entry_nums[i]:
            matches+=1
    return matches*/
var function pic6() {
    let numbers = []
    for (let i=0; i<6; i++) {
        //console.log(i)
        let number = Math.floor(Math.random() * 100)
        //console.log(numbers)
        numbers.push(number)
        //console.log(numbers);
    }return numbers
}
console.log(pic6())

function numMatches(){
    let winningNums = pic6();
    let entryNums =  pic6();
    let matches = 0;
    for (let i=0; i<6; i++)
        if 
}

/* let a = parseFloat(prompt("first number"))
let b = parseFloat(prompt("second number"))

alert(`the answer is ${a+b}`) */