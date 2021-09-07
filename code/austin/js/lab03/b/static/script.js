class ATM {
    constructor(balance=0, interest=.001) {
      this.balance = balance
      this.interest = interest
      this.transactions = []
      this.interestAccrued = 0
    }getBalance(){
        return this.balance
    }deposit(amount){
        this.balance += parseFloat(parseFloat(amount).toFixed(2))
        this.transactions.push(`Deposited $${amount}`)
    }checkWithdrawal(amount){
        if(this.balance > amount){
            return true
        }else{
            return false
        } 
    }withdrawal(amount){
        this.balance -= parseFloat(parseFloat(amount).toFixed(2))
        this.transactions.push(`Withdrew $${amount}`)
    }calcInterest(){
        this.interestAccrued = parseFloat((this.balance * this.interest).toFixed(2))
        this.balance += this.interestAccrued
    }printTrans(){
        return this.transactions
    }

}

var atm = new ATM()
let depositBtn = document.getElementById("deposit")
let withdrawalBtn = document.getElementById("withdrawal")
let interestBtn = document.getElementById("interest")
var showBal = document.getElementById("showBal")
let button = document.getElementsByClassName("button")
var num = document.getElementById("number")
console.log(button)
depositBtn.addEventListener("click", function(event) {
    event.preventDefault()
    atm.deposit(parseFloat(num.value))
    let bal = atm.balance
    let displayBal =document.getElementById("balance")
    displayBal.innerText = "Balance: $" + bal
    //let transList = document.getElementById("transList")
    let node =document.createElement("li")
    let numstr = num.value
    let textnode = document.createTextNode("Deposited -- $" + numstr)
    node.appendChild(textnode)
    document.getElementById("transList").appendChild(node)
    console.log(parseFloat(num.value))
    console.log(atm.transactions)
    console.log(number)
    })
withdrawalBtn.addEventListener("click", function(event) {
    event.preventDefault()
    atm.withdrawal(parseFloat(num.value))
    let bal = atm.balance
    let displayBal =document.getElementById("balance")
    displayBal.innerText = "Balance: $" + bal
    let node =document.createElement("li")
    let numstr = num.value
    let textnode = document.createTextNode("Withdrew -- $" + numstr)
    node.appendChild(textnode)
    document.getElementById("transList").appendChild(node)
    })
interestBtn.addEventListener("click", function(event) {
    event.preventDefault()
    atm.calcInterest()
    let bal = atm.balance
    let displayBal =document.getElementById("balance")
    displayBal.innerText = "Balance: $" + bal
    let node =document.createElement("li")
    let numstr = atm.interestAccrued
    let textnode = document.createTextNode("Interest accrued-- $" + numstr)
    node.appendChild(textnode)
    document.getElementById("transList").appendChild(node)
    })

/*while(true){
    //let command = prompt("Enter a command:")
    if(command ==="balance" ){
       // alert(`Balance: ${atm.getBalance()}`)
    }else if(command ==="deposit"){
        let depositAmount =prompt("How much would you like to deposit?")
        if (depositAmount >= 0.01){
            atm.deposit(depositAmount)
            //alert(`Deposited: $${parseFloat(depositAmount).toFixed(2)}\nNew balance is: $${atm.getBalance()}`)
        }else{
            alert("Not a valid number, please try again.")
        }
    }else if(command === "withdrawal"){
        //let withdrawalAmount = prompt("How much would you like to withdrawal?")
        if(withdrawalAmount >= 0.01){
            if(atm.checkWithdrawal(withdrawalAmount)){
                atm.withdrawal(withdrawalAmount)
            //alert(`Withdrew: $${parseFloat(withdrawalAmount).toFixed(2)}\nNew balance is: $${atm.getBalance()}`)
            }else{
                //alert("Not enough funds!")
            }
        }else{
            //alert("Not a valid number!")
        }
    }else if(command === "interest"){
        amount = atm.calcInterest()
        atm.deposit(amount)
        //alert(`Accumulated $${amount} in interest`)
    }else if(command === "transactions"){
        //alert(`Transaction history:\n ${atm.transactions}`)
    }else if(command === "exit"){
        break
    }else{
        //alert("Not a valid command!")
    }
}*/