/**************************************************************
 * Author: Jeremy Bush
 * Project: Programming Bootcamp, JavaScript Lab 3b
 * Version: 1
 * Date: 7/7/2021
 *************************************************************/

// Set up basic HTML stuff
let h1 = document.createElement("h1");
let input = document.createElement("input");
let form = document.createElement("form");
var btn = document.createElement("button");
let body = document.body
// List of box IDs
var boxList = [];
// variable to know howe many boxes exist.
var totalBoxes = 0;


// Place title.
h1.innerText = "Average Calculator";
body.appendChild(h1);

// put add button on form.
btn.innerHTML = "+";
btn.setAttribute("onclick", "addBtn()");
body.appendChild(btn);

// add button for calculating average.
body.appendChild(document.createElement("br"));
let calcAvg = document.createElement("button");
calcAvg.innerHTML = "Calculate";
calcAvg.setAttribute("onclick", "avg()")
body.appendChild(calcAvg);
body.appendChild(document.createElement("br"));

// Create function that adds input box when clicked.
function addBtn(){
    let currentNum = "num".concat(totalBoxes);
    let tmpInput = document.createElement("input");
    tmpInput.type = "number";
    tmpInput.name = currentNum;
    tmpInput.id = currentNum;
    body.appendChild(tmpInput);
    // create the delete button and add to the form after the input.
    let tmpDel = document.createElement("button")
    tmpDel.innerHTML = "-";
    tmpDel.name = "del_".concat(currentNum);
    tmpDel.id = "del_".concat(currentNum);
    tmpDel.setAttribute("onclick", "delBtn(this.id)");
    body.appendChild(tmpDel);
    // Add box ID to boxList.
    boxList.push(currentNum);
    // increment totalBoxes to prepare for the next box to be added.
    totalBoxes++;
}


// Create function that deletes an input box
function delBtn(del_btnId){
    let boxToDel = document.getElementById(del_btnId.split("_").pop());
    let btnToDel = document.getElementById(del_btnId);
    let breakToDel = document.getElementById("br_".concat(del_btnId.split("_").pop()));
    boxToDel.remove();
    btnToDel.remove();
    breakToDel.remove();
    // remove box to be deleted from boxList.
    let index = boxList.indexOf(boxToDel);
    boxList.splice(index, 1);
}

function avg(){
    let sum = 0;
    for (box of boxList){
        sum = sum + parseInt(document.getElementById(box).value);
    }
    let average = sum/boxList.length;
    let p = document.createElement("p");
    p.innerHTML = "The average of the numbers you entered is ".concat(average);
    body.appendChild(p)
}

