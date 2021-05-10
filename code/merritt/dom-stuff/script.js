let myDiv = document.getElementById("mydiv");
let thisDiv = document.getElementById("thisdiv");
let thatDiv = document.getElementById("thatdiv");





let form = document.createElement('form');
form.action = 'link/to/post/to/';
form.method = 'post';

let inputText = document.createElement('input');
inputText.type = 'text';
inputText.name = 'query';
inputText.placeholder = 'Query';
inputText.required = true;
inputText.addEventListener('input', function(e) {
  console.log(this.value);
});

let submitBtn = document.createElement('input');
submitBtn.type = 'submit';
submitBtn.addEventListener('click', function(e) {
  e.preventDefault();
  alert("fooled you!");
});

form.appendChild(inputText);
form.appendChild(submitBtn);

document.getElementsByTagName('body')[0].appendChild(form);




let weatherResults = [
  {high: 78, low: 53, conditions: 'sunny'},
  {high: 86, low: 61, conditions: 'rainy'},
  {high: 45, low: 32, conditions: 'partly cloudy'},
  {high: 67, low: 45, conditions: 'partly sunny'},
  {high: 174, low: 159, conditions: 'deadly'}
]

let weatherResultsDiv = document.createElement('div');

weatherResults.forEach(function(day, i) {
  let dayP = document.createElement('p');
  dayP.innerText = `DAY ${i + 1}: High of ${day.high}, low of ${day.low}. Day ${i + 1} is looking ${day.conditions}.`;
  dayP.addEventListener('mouseenter', function(e) {
    this.style.backgroundColor = 'darkred';
    this.style.color = 'white';
  });
  dayP.addEventListener('mouseleave', function(e) {
    this.style.backgroundColor = 'inherit';
    this.style.color = 'inherit';
  });
  weatherResultsDiv.appendChild(dayP);
});

document.getElementsByTagName('body')[0].appendChild(weatherResultsDiv);







function callback(e) {
  console.log(e);
  if (e.button === 0) {
      alert("You clicked the left mouse button!");
  } else if (e.button === 2) {
      alert("You clicked the right mouse button!");
  } else {
      alert("You clicked a mouse button, but it wasn't the left or right!");
  }
}
function superCoolCallback(e) {
  console.log(this);
  this.innerText = "clicked!";
}
let bt = document.querySelector('#bt');
bt.addEventListener('click', superCoolCallback);

// document.body.addEventListener("keydown", function(e) {
//   console.log(e.keyCode);
// });




let intervalBtns = document.getElementsByClassName("time");
for (let i = 0; i < intervalBtns.length; i++) {
  let counter = 0;
  let interval;
  function logger() {
    // if (counter > 8) {
    //   clearInterval(interval);
    // };
    console.log(`button number ${i+1}`)
    counter++;
  }
  intervalBtns[i].addEventListener('click', function() {
    clearInterval(interval);
    logger();
    interval = setInterval(logger, (i+1) * 1000);
  });
}