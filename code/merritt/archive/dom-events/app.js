let pHelloWorld = document.getElementById("hello-world");
let textyMctextface = document.getElementsByName("textymctextface")[0];
let superCoolElements = document.getElementsByClassName("super-cool-element");
let li = document.getElementsByTagName("li");

let textBlocks = document.querySelectorAll("li, p");

textBlocks.forEach(function(textBlock) {
  textBlock.innerHTML += "<h1>Yup.</h1>";
});

pHelloWorld.innerText = "Nope.";
pHelloWorld.id = "nope"
pHelloWorld.style.backgroundColor = "darkred";
pHelloWorld.style.fontSize = "24px";
pHelloWorld.setAttribute("id", "no-no-no");

let div = document.createElement("div");
div.style.backgroundColor = "lightgreen";
div.style.padding = "12px";


let btn = document.createElement("button");
btn.style.backgroundColor = "lightblue";
btn.style.border = "1px solid white";
btn.innerText = 'click';

div.appendChild(btn);

let ol = document.getElementsByTagName('ol')[0];
ol.appendChild(div);


function callback(event) {
  if (event.button === 0) {
      alert("You clicked the left mouse button!");
  } else if (event.button === 2) {
      alert("You clicked the right mouse button!");
  } else {
      alert("You clicked a mouse button, but it wasn't the left or right!");
  }
  console.log(event);
}
btn.addEventListener('click', callback);




let freeIpadSsn = document.getElementById("free-ipad-ssn");
let freeIpadBtn = document.getElementById("free-ipad-btn");
let freeIpadResult = document.getElementById("free-ipad-result");

function callback(e) {
  freeIpadResult.innerText = `No ipad for you! Only identity theft! I know that your social security numebr is ${freeIpadSsn.value}. How could you be so foolish!`;
  freeIpadResult.style.backgroundColor = "black";
  freeIpadResult.style.color = "white";
}


freeIpadBtn.addEventListener("click", callback);

freeIpadSsn.addEventListener("keydown", function(e) {
  if (e.keyCode === 13) {
    callback(e);
  }; 
});

freeIpadSsn.addEventListener('input', function(e){
  freeIpadResult.style.backgroundColor = "white";
  freeIpadResult.style.color = "black";
  if (9 - freeIpadSsn.value.length === 9) {
    freeIpadResult.innerText = `Wait wait! Type in your social security number. Trust me! I know you want iPad! Totally secure!`;
  } else if (9 - freeIpadSsn.value.length === 0) {
    freeIpadResult.innerText = `Yes! Yes! Hit button! I know you want iPad! Totally secure!`;
  } else if (9 - freeIpadSsn.value.length < 0) {
    freeIpadResult.innerText = `Wait wait! Is not social security number! I know America social security has nine numbers. You not smarter than very legit honest hacker. I know you want iPad! Totally secure!`;
  } else {
    freeIpadResult.innerText = `Wait wait! Keep typing! Is ${9 - freeIpadSsn.value.length} more numbers! I know you want iPad! Totally secure!`;
  }
});