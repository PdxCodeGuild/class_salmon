let btns = document.getElementsByClassName("btn");

// for (let i=0; i < btns.length; i++) {
//     btns[i].addEventListener("click", function() {
//         let interval = setInterval(function() {
//             console.log(i);
//         }, i*1000);
//         let cancel = document.createElement("button");
//         cancel.innerText = "cancel";
//         cancel.addEventListener("click", function() {
//             clearInterval(interval);
//             cancel.remove();
//         });
//         document.body.append(cancel);
//     });
// }

for (let i=0; i < btns.length; i++) {
    btns[i].onclick = function() {
        let interval = setInterval(function() {
            console.log(i);
        }, i*1000);
        btns[i].onclick = function() {
            clearInterval(interval);
            interval = setInterval(function() {
                console.log(i);
            }, i*1000);
        }
    };
}

