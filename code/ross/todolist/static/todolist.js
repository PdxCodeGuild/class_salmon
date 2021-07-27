function newItem() {
    var itemName = document.querySelector("#add-item");
    var firstList = document.querySelector("#list1");
    // console.log()
    var listItem = document.createElement("li");
    console.log("itemName: " + itemName.value)
    listItem.innerHTML = itemName.value;
    console.log("listItem: " + listItem.innerHTML)
    var completeButton  = document.createElement("button");
    completeButton.innerHTML = "complete";
    var completeList = document.querySelector("#list2")
    console.log("complete list: " + completeList)
    console.log("parentNode: " + this.parentNode)
    completeButton.setAttribute("onclick", "completeList.appendChild(this.parentNode);");
    console.log(completeButton);
    listItem.appendChild(completeButton);
    var removeButton  = document.createElement("button");
    removeButton.innerHTML = "remove";
    removeButton.setAttribute("onclick", 'return this.parentNode.remove()');
    removeButton.setAttribute("class", "remove-btn")
    console.log(removeButton);
    listItem.appendChild(removeButton);
    listItem.setAttribute("id" , itemName)
    firstList.appendChild(listItem);
    console.log("first list: " + firstList)
    console.log("listitem: " + listItem)
    itemName.value = ''
    completeButton.addEventListener("click", function(){
        completeList.appendChild(listItem)
        listItem.removeChild(completeButton)
    })
}