function newItem() {
    var item = document.createElement("li")
    var itemName = document.getElementById("add-item").value
    var text = document.createTextNode(itemName)
    item.appendChild(text)
}