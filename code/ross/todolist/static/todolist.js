function newItem() {
    //var item = document.createElement("li")
    let x = document.createElement("INPUT");
    x.setAttribute("type", "checkbox");
    x.setAttribute("name", "todo");
    let itemName = document.getElementById("add-item").value
    console.log(itemName)
    x.setAttribute("value", itemName);
    let text = document.createTextNode(itemName)
    //item.appendChild(text)
    document.getElementById("list1").appendChild(x)
    console.log(x)
    let y = document.createElement("label")
    y.setAttribute("for", itemName)
    y.innerHTML = itemName
    document.getElementById("list1").appendChild(y)
    console.log(y)
}