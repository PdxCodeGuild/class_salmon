/*class ATM:
    def __init__(self, balance=0, interest=.001):
        self.balance = balance
        self.interest = interest
        self.transaction = []
    def check_balance(self):# returns the account balance
        return self.balance
    def deposit(self,amount): #deposits the given amount in the account
        self.balance = self.balance + amount
        self.transaction.append(f'user deposited ${amount}')
        print(self.transaction)
        return amount
    def check_withdrawal(self,amount): #returns true if the withdrawn amount won't put the account in the negative
        if self.balance >= amount:
            return True
        else:
            return False
    def withdraw(self,amount): #withdraws the amount from the account and returns it
        self.balance -= amount
        self.transaction.append(f'user withdrew ${amount}')
        print(self.transaction)
        return amount
    def calc_interest(self): #returns the amount of interest calculated on the account
        interest_accrued = self.balance * self.interest
        return interest_accrued
    def print_transactions(self):
        return self.transaction
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
print('Available commands:')
print('balance  - get the current balance')
print('deposit  - deposit money')
print('withdraw - withdraw money')
print('interest - accumulate interest')
print('transactions - see a list of transactions')
print('exit     - exit the program')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'transactions':
        print(atm.print_transactions())
    elif command == 'exit':
        break
    else:
        print('Command not recognized')*/
class ATM {
    constructor(balance=0, interest=.001) {
      this.balance = balance
      this.interest = interest
      this.transactions = []
    }getBalance() {
      return this.balance
    }deposit(amount){
        this.balance += parseFloat(parseFloat(amount).toFixed(2))
        this.transactions.push(`Deposited $${amount}\n`)
    }checkWithdrawal(amount){
        if(this.balance > amount){
            return true
        }else{
            return false
        } 
    }withdrawal(amount){
        this.balance -= parseFloat(parseFloat(amount).toFixed(2))
        this.transactions.push(`Withdrew $${amount}\n`)
    }calcInterest(){
        let interestAccrued = parseFloat((this.balance * this.interest).toFixed(2))
        return interestAccrued
    }printTrans(){
        
        alert(`Transaction history:\n ${this.transactions}`)
    }

}
let atm = new ATM()
console.log(atm)
alert("Welcome to the ATM")
while(true){
    alert("Available commands:\nbalance  - get the current balance\ndeposit  - deposit money\nwithdraw - withdraw money\ninterest - accumulate interest\ntransactions - see a list of transactions\nexit     - exit the program")
    let command = prompt("Enter a command:")
    if(command ==="balance" ){
        alert(`Balance: ${atm.getBalance()}`)
    }else if(command ==="deposit"){
        let depositAmount =prompt("How much would you like to deposit?")
        if (depositAmount >= 0.01){
            atm.deposit(depositAmount)
            alert(`Deposited: $${parseFloat(depositAmount).toFixed(2)}\nNew balance is: $${atm.getBalance()}`)
        }else{
            alert("Not a valid number, please try again.")
        }
    }else if(command === "withdrawal"){
        let withdrawalAmount = prompt("How much would you like to withdrawal?")
        if(withdrawalAmount >= 0.01){
            if(atm.checkWithdrawal(withdrawalAmount)){
                atm.withdrawal(withdrawalAmount)
            alert(`Withdrew: $${parseFloat(withdrawalAmount).toFixed(2)}\nNew balance is: $${atm.getBalance()}`)
            }else{
                alert("Not enough funds!")
            }
        }else{
            alert("Not a valid number!")
        }
    }else if(command === "interest"){
        amount = atm.calcInterest()
        atm.deposit(amount)
        alert(`Accumulated $${amount} in interest`)
    }else if(command === "transactions"){
        alert(`Transaction history:\n ${atm.transactions}`)
    }else if(command === "exit"){
        break
    }else{
        alert("Not a valid command!")
    }
}