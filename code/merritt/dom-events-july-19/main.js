let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let operand = document.getElementById("operand");
let calcButton = document.getElementById("calc-button");
let answerP = document.getElementById("answer");

function callback(e) {
  console.log(e);
  let result;
  let n1 = parseInt(num1.value);
  let n2 = parseInt(num2.value);
  if (operand.value === '+') {
    result = n1 + n2;
  } else if (operand.value === '-') {
    result = n1 - n2;
  } else if (operand.value === '*') {
    result = n1 * n2;
  } else if (operand.value === '/') {
    result = n1 / n2;
  }
  answerP.innerText = result;
}

function callback2() {
  alert('body of function');
  return function() {alert('return function')};
}

function keyPress(e) {
  if (e.which === 13) {
    callback(e);
  }
}

calcButton.addEventListener('click', callback);

num1.addEventListener('keydown', keyPress);
num2.addEventListener('keydown', keyPress);

// num1.addEventListener('input', callback);
// num2.addEventListener('input', callback);
// operand.addEventListener('input', callback);

num1.addEventListener('change', callback);
num2.addEventListener('change', callback);
operand.addEventListener('change', callback);