let newPost = document.getElementById("new-post");
let submit = document.getElementById("submit");
let target = document.getElementById("target");
let deleteSelectedButton = document.getElementById("delete-selected");

submit.addEventListener('click', function(event) {
    event.preventDefault();
    let postBody = newPost.value;

    let div = document.createElement("section");
    // div.style.border = "1px solid black";
    // div.style.width = "640px";
    // div.style.minHeight = "160px";
    div.classList.add("post");

    let editButton = document.createElement("button");
    let deleteButton = document.createElement("button");
    let pBody = document.createElement("p");
    let pTimeStamp = document.createElement("p");
    let deleteCheckBox = document.createElement("input");

    editButton.innerText = "Edit Me";
    editButton.addEventListener('click', function() {
        // let bodyValue = this.nextSibling.nextSibling.value;
        // let bodyValue = this.parentElement.querySelectorAll("p")[0];
        let bodyValue = pBody.innerText;
        pBody.style.display = "none";
        let editBox = document.createElement("textarea");
        editBox.value = bodyValue;
        editBox.style.display = "block";
        editBox.style.width = "100%";
        editBox.style.height = "auto";
        div.insertBefore(editBox, pBody);

        editButton.disabled = true;

        let postButton = document.createElement("button");
        postButton.innerText = "Done Editing";
        postButton.addEventListener('click', function() {
            pBody.innerText = editBox.value;
            pBody.style.display = "block";
            editBox.remove();
            editButton.disabled = false;
            postButton.remove();
        });
        div.insertBefore(postButton, editButton);

    });
    div.append(editButton);

    deleteButton.innerText = "Delete Me";
    deleteButton.addEventListener('click', function() {
        this.parentElement.remove();
    });
    // div.append(deleteButton);

    deleteCheckBox.type = "checkbox";
    deleteCheckBox.classList.add("delete-checkbox");
    div.append(deleteCheckBox);

    pBody.innerText = postBody;
    div.append(pBody);

    pTimeStamp.innerText = new Date().toString();
    pTimeStamp.style.textAlign = "right";
    div.append(pTimeStamp);

    target.insertBefore(div, target.firstChild);

});

deleteSelectedButton.addEventListener('click', function() {
    let checkboxes = target.querySelectorAll("input[type='checkbox'].delete-checkbox");
    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            checkboxes[i].parentElement.remove()
        }
    }
});