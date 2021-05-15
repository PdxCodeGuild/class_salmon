let p = document.getElementsByTagName("p");
let red = document.getElementsByClassName("red");
let blue = document.getElementsByClassName("blue");
let title = document.getElementById("title");

// title.innerHTML = "<strong><em>Hello World!</em></strong>";

for (let i=0; i<red.length; i++) {
    red[i].innerText = "Why is this text not red? We'll have to fix that...";
    red[i].style.backgroundColor = "red";
    red[i].style.color = "white";
    red[i].style.border = "1px solid black";
}

let div = document.createElement("div");
div.id = "js";
div.style.width = "400px";
div.style.height = "400px";
div.style.border = "2px dashed black";

let img = document.createElement("img");
img.src = "bert.gif";
img.style.maxWidth = "100%";
img.style.margin = "24px";

div.appendChild(img);

title.appendChild(div);

// title.innerHTML += "<p>paragraph</p>";

div = document.getElementById("js");
div.style.backgroundColor = "red";

// console.log(div);
// console.log(img);

div.addEventListener('click', function(event) {
    console.log(event.x, event.y)
});

function my_super_cool_callback(event) {
    console.log(event.x, event.y)
}
div.addEventListener('click', my_super_cool_callback);

// function my_super_cool_callback() {
//     alert("this is the function");
//     return function() {
//         alert("this is the return")
//     }
// }
// div.addEventListener('click', my_super_cool_callback()); 


///////////////////////////////////////////////////////////////////////////


let btn = document.getElementById("btn");
let more = document.getElementById("more");
// let num1 = document.getElementById("num1");
// let num2 = document.getElementById("num2");
let nums = document.getElementsByClassName("num");
let results = document.getElementById("results");
let inputs = document.getElementById("inputs");

let numCounter = 3;

// num1 = parseFloat(num1.value)
// num2 = parseFloat(num2.value)

// console.log(nums)

function doMath(e) {
    let li = document.createElement("li");
    let nums = document.getElementsByClassName("num");
    let sum = 0
    for (let i=0; i<nums.length; i++) {
        if (nums[i].value) {
            sum += parseFloat(nums[i].value)
        }
    }
    li.innerText = sum;
    // li.innerText = `${nums[0].value} + ${nums[1].value} = ${parseFloat(nums[0].value) + parseFloat(nums[1].value)}`;
    // li.innerText = `${num1.value} + ${num2.value} = ${parseFloat(num1.value) + parseFloat(num2.value)}`
    // li.innerText = `${num1} + ${num2} = ${num1 + num2}`
    results.appendChild(li);
}

btn.addEventListener('click', doMath);

more.addEventListener('click', function(e) {
    let newInput = document.createElement("input");
    newInput.type = "number";
    newInput.placeholder = `Number ${numCounter}`;
    numCounter++;
    newInput.classList.add("num");

    newInput.addEventListener('keydown', function(e) {
        if (e.key === "Enter") {
            doMath(e);
        }
    });
    // newInput.addEventListener('input', doMath);

    let btn = document.createElement("button");
    btn.innerText = "×";
    btn.addEventListener('click', function(e) {
        this.previousSibling.remove();
        this.nextSibling.remove();
        this.remove();
    });

    inputs.append(" + ");
    inputs.appendChild(newInput);
    inputs.appendChild(btn);
});

/////////////////////////////////////////////////////////////////////////////

let dot = document.getElementById("dot");
let box = document.getElementById("box");

let mouse_down = false;

box.addEventListener("mousemove", function(e) {
    if (mouse_down) {
        dot.style.left = (e.clientX - 8) + "px";
        dot.style.top = (e.clientY - 8) + "px";
    }
});

box.addEventListener("mousedown", function(e) {
    mouse_down = true;
});

box.addEventListener("mouseup", function(e) {
    mouse_down = false;
});