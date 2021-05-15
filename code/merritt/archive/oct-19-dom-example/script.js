let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let oper = document.getElementById("oper");
let btn = document.getElementById("calc-btn");
let results = document.getElementById("results");

function callback2() {
  alert('body of function');
  return function() {alert('return function')};
}
 
function doTheMath() {
  let x = parseFloat(num1.value);
  let y = parseFloat(num2.value);
  let answer;
  if (oper.value === "+") {
    answer = x + y;
  } else if (oper.value === "-") {
    answer = x - y;
  } else if (oper.value === "*") {
    answer = x * y;
  } else if (oper.value === "/") {
    answer = x / y;
  }
  // let li = document.createElement("li");
  // li.innerText = answer;
  // results.appendChild(li);
  if (answer) {
    results.innerText = answer;
  }
}

btn.addEventListener('click', callback2);
num1.addEventListener('input', doTheMath);
num2.addEventListener('input', doTheMath);
oper.addEventListener('input', doTheMath);


// num2.addEventListener('keydown', function(event) {
//   if (event.key === "Enter") {
//     doTheMath();
//   }
// });


// btn.addEventListener('click', function() {
//   let x = parseFloat(num1.value);
//   let y = parseFloat(num2.value);
//   let answer;
//   if (oper.value === "+") {
//     answer = x + y;
//   } else if (oper.value === "-") {
//     answer = x - y;
//   } else if (oper.value === "*") {
//     answer = x * y;
//   } else if (oper.value === "/") {
//     answer = x / y;
//   }
//   let li = document.createElement("li");
//   li.innerText = answer;
//   results.appendChild(li);
// });

let myArray = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1];

let sumOfSquaredGreaterThanSixEveryOtherDouble = myArray.map(function(x, i, originalArray) {
  if (i % 2 === 0) {
    return x*2;
  }
  return x;
}).filter(function(x) {
  return x > 6;
}).map((x, i, originalArray) => x**2).reduce(function(runningTotal, x) {
  return runningTotal + x;
}, 0);

// function(x) {
//   return x**2;
// }

console.log(sumOfSquaredGreaterThanSixEveryOtherDouble);








let timedBtns = document.getElementsByClassName("timed-btn");

for (let i=0; i < timedBtns.length; i++) {
  timedBtns[i].addEventListener("click", function() {
    let interval = setInterval(function() {
      // cancel.remove();
      console.log(i);
    }, i*1000);
    let cancel = document.createElement("button");
    cancel.innerText = "cancel";
    cancel.addEventListener("click", function() {
      clearInterval(interval);
      cancel.remove();
    });
    document.body.append(cancel);
  });
}