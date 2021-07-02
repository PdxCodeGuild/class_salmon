let first_card = prompt('What\'s your first card, playa?', 'first card');
let second_card = prompt('What\'s your second card, playa?', 'second card');
let third_card = prompt('What\'s your third card, playa?', 'third card');
const card_val = {A: 1,
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
let sum_cards = (card_val[first_card] +
             card_val[second_card] + card_val[third_card]);

if (sum_cards < 17) {
    let advice = "You should hit.";
} else if (sum_cards >= 17 and sum_cards < 21) {
    let advice = "You should stay.";
} else if (sum_cards == 21) {
    let advice = "BLACKJACK, BABY!!!";
} else if (sum_cards > 21) {
    let advice = "Daww... BUST!";
}
alert(`You've got ${sum_cards}. 
${advice}`)
