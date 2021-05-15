let id = document.getElementById("mycoolp");
let body = document.getElementsByTagName("body")[0];
let tagname = document.getElementsByTagName("p");
let byclass = document.getElementsByClassName("coolps");
let query = document.querySelector("p");
let queryset = document.querySelectorAll("#mycoolp");

let text1 = document.getElementById("text1");
let button1 = document.getElementById("button1");

console.log(id.innerText);
console.log(id.innerHTML);

console.log(body.innerText);
console.log(body.innerHTML);

id.style.backgroundColor = "red";
id.id = "merritt";

id.setAttribute("rad", "yes");
id.setAttribute("class", "yes no maybe");
console.log(id.getAttribute("rad"));


let ul = document.createElement("ul");
ul.style.backgroundColor = "darkred";
ul.style.listStyle = "none";
ul.style.color = "white";

for (let i=0; i<6; i++) {
  let li = document.createElement("li");
  li.innerText = `This is list item #${i+1}`;
  ul.appendChild(li);
}


body.appendChild(ul);

let li3 = document.getElementsByTagName("li")[2];
li3.innerText = "Bullet Points!";

function callback(e) {
  e.preventDefault();
  // let p = document.createElement("p");
  // p.innerText = text1.value;
  // body.appendChild(p);
  let p = document.getElementById("result");
  p.innerText = text1.value;
}

button1.addEventListener('click', callback);

let timeoutButtons = document.getElementsByClassName("timeout");
for (let i = 0; i < timeoutButtons.length; i++) {
  timeoutButtons[i].addEventListener("click", function(e) {
    setInterval(function() {
      console.log(i);
    }, i*1000);
  });
}