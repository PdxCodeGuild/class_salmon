let firstCard = document.querySelector('#firstCard')
let secondCard = document.querySelector('#secondCard')
let thirdCard = document.querySelector('#thirdCard')
let output_div = document.querySelector('#output_div');
let output_div2 = document.querySelector('#output_div2');
let output_div3 = document.querySelector('#output_div3');
let output_div4 = document.querySelector('#output_div4');
let final = document.querySelector('#final');

final.onclick = function(evt) {
    let sumCards = 0
    sumCards += cardVal[firstCard.value]  
    sumCards += cardVal[secondCard.value]
    sumCards += cardVal[thirdCard.value]
    let advice 
    if (sumCards < 17) {
        advice = "You should hit.";
    } else if (sumCards >= 17 && sumCards < 21) {
        advice = "You should stay.";
    } else if (sumCards == 21) {
        advice = "BLACKJACK, BABY!!!";
    } else if (sumCards > 21) {
        advice = "Daww... BUST!";
    }
    output_div4.innerText = 'You got ' + sumCards + '...' + advice;

}

const cardVal = {A: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            J: 10,
            Q: 10,
            K: 10
            };
