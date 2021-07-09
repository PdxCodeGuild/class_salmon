let firstCard = prompt('What\'s your first card, playa?', 'first card');
let secondCard = prompt('What\'s your second card, playa?', 'second card');
let thirdCard = prompt('What\'s your third card, playa?', 'third card');
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
let sumCards = (cardVal[firstCard] +
             cardVal[secondCard] + cardVal[thirdCard]);
             
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
alert(`You've got ${sumCards}. 
${advice}`)

