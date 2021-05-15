class ATM {
    constructor(balance=0) {
        this.balance = balance;
        this.transactions = [];
    }

    check_balance() {
        return this.balance;
    }

    deposit(amount) {
        this.balance += amount;
        this.transactions.push(`Deposit of $${amount}: New balance $${this.balance}`);
    }

    check_withdrawl(amount) {
        return this.balance >= amount;
    }

    withdrawl(amount) {
        if (this.check_withdrawl(amount)) {
            this.balance -= amount;
            this.transactions.push(`Withdrawl of $${amount}: New balance $${this.balance}`);
        } else {
            this.balance -= amount;
            this.balance -= 35;
            this.transactions.push(`Withdrawl of $${amount} --- OVERDRAFT FEE: $35 --- New balance $${this.balance}`);
        }
    }

    print_transactions() {
        return this.transactions;
    }

}

let account = new ATM();

let balanceElement = document.getElementById("current-balance");
let historyElement = document.getElementById("transaction-history");

let depositAmount = document.getElementById("deposit-amount");
let withdrawlAmount = document.getElementById("withdrawl-amount");
let submitDeposit = document.getElementById("submit-deposit");
let submitWithdrawl = document.getElementById("submit-withdrawl");

function update() {
    balanceElement.innerText = `$${account.check_balance()}`;
    historyElement.innerHTML = "";
    account.print_transactions().forEach(function(transaction) {
        let li = document.createElement("li");
        li.innerText = transaction;
        li.addEventListener("click", function() {
            alert(this.innerText);
        });
        historyElement.append(li);
    });
}

update();

submitDeposit.addEventListener("click", function() {
    let amount = parseFloat(depositAmount.value);
    account.deposit(amount);
    depositAmount.value = "";
    update();
});

submitWithdrawl.addEventListener("click", function() {
    let amount = parseFloat(withdrawlAmount.value);
    account.withdrawl(amount);
    withdrawlAmount.value = "";
    update();
});

// withdrawlAmount.addEventListener("input", function() {
//     if (account.check_withdrawl(this.value)) {
//         submitWithdrawl.removeAttribute("disabled");
//     } else {
//         submitWithdrawl.setAttribute("disabled", "true");
//     }
// });