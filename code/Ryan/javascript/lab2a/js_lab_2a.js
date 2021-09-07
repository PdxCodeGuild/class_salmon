const card_picks = []

let i = 0;
while(i < 3) {
    const user_pick = prompt("Enter a card");
    
    if(user_pick === "j" || user_pick === "q" || user_pick === "k"){
        card_picks.push(Number(10));
    } 
        else if(user_pick === "a"){
        card_picks.push(Number(1));
        } 
    else{
        card_picks.push(Number(user_pick));
        }

    i++;
}

// console.log(card_picks)

let card_total = 0
for(let card of card_picks){
    card_total += card
}

// console.log(card_total)

if(card_total > 21){
    alert(`${card_total} Already Busted!`);
} else if(card_total === 21){
    alert(`${card_total} Blackjack!!!`);
} else if(card_total < 21 && card_total > 16){
    alert(`${card_total} Stay`)
} else{
    alert(`${card_total} Hit`)
}