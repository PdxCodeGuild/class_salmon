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
    listItem.appendChild(completeButton);
    //firstList.appendChild(itemName.value);
    var removeButton  = document.createElement("button");
    removeButton.innerHTML = "remove";
    removeButton.setAttribute("onclick", "removeStuff()");
    removeButton.setAttribute("class", "remove")
    console.log(removeButton);
    listItem.appendChild(removeButton);
    listItem.setAttribute("id" , itemName)
    firstList.appendChild(listItem);
    // let br = document.createElement("br");
    // firstList.appendChild(br);
    console.log(firstList)
}

function completed(event) {
    event.preventDefault();

}


function removeStuff(event) {
    event.preventDefault();
    firstList.parentNode.removeChild(listItem)

    // let close = document.getElementsByClassName("remove")
    // for(let i = 0;i <close.length;i++){
    //     close[i].onclick = function(){
    //         var div = this.parentElement;
    //         div.style.display = "none";
    //     }
    // }
    
}
// Click on a close button to hide the current list item
// var close = document.getElementsByClassName(“close”);
// var i;
// for (i = 0; i < close.length; i++) {
//  close[i].onclick = function() {
//     var div = this.parentElement;
//    div.style.display = “none”;
//  }
// }
// span.className = “close”;
