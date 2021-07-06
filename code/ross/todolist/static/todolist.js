function newItem() {
    var itemName = document.querySelector("#add-item");
    //var item = document.createElement("li")
    // x.setAttribute("id", itemName);
    // x.setAttribute("class", itemName);
    // console.log(itemName);
    // x.setAttribute("value", itemName);
    // let text = document.createTextNode(itemName);
    //item.appendChild(text)
    var firstList = document.querySelector("#list1");
    var listItem = document.createElement("li");
    listItem.innerHTML = itemName.value;
    firstList.appendChild(listItem);
    // var y = document.createElement("label");
    // y.setAttribute("for", itemName);
    // y.setAttribute("class", itemName);
    // y.setAttribute("id", itemName);
    // y.innerHTML = itemName;
    // var something2 = document.getElementById("#list1").appendChild(y);
    // console.log(y);
    var completeButton  = document.createElement("button");
    completeButton.innerHTML = "complete";
    completeButton.setAttribute("onclick", "completed()");
    console.log(completeButton);
    firstList.appendChild(completeButton);
    firstList.appendChild(itemName.value);
    var removeButton  = document.createElement("button");
    removeButton.innerHTML = "remove";
    removeButton.setAttribute("onclick", "removeStuff()");
    console.log(removeButton);
    firstList.appendChild(removeButton);
    // let br = document.createElement("br");
    // firstList.appendChild(br);
}

function completed() {
    event.preventDefault();

}


function removeStuff() {

    event.preventDefault();
    let itemVal = document.querySelector('input[type="checkbox"]:checked').value
    console.log(itemVal)
    let itemClass = document.getElementsByClassName(itemVal);
    console.log(itemClass)
    // itemClass.remove()
    
}
