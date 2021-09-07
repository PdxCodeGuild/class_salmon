// User text input
let entry_input = document.querySelector("#input-box");

// Define lists
// list_inProgress = ["test", "test2", "test3"];
// list_Completed = ["test", "test2", "test3"];

// Define Buttons
let add_btn = document.querySelector("#add-btn");
let completed_btn = document.querySelector("#completed-btn");
let remove_btn = document.querySelector("#remove-btn");

// Define Output List
let output_inProgress = document.querySelector("#uncompleted");

// // Output lists
// for(let i = 0; i < list_inProgress.length; i++){
//     document.createElement;
// }

// Check Checkboxes

// On Add button click
add_btn.addEventListener("click", function(){
    // Create the list item
    const li = document.createElement("li");

    // Get value for the list item
    const li_value = document.querySelector("#input-box").value;

    // Change the list item into a child Node
    const text = document.createTextNode(li_value);

    // Assign value to the list item
    li.appendChild(text);

    console.log(li,li_value,text)
    document.querySelector("uncompleted").appendChild(li);

})

// On Completed click
completed_btn.addEventListener("click", function(){
    // Strike through item
})


// On Remove click
remove_btn.addEventListener("click", function(){
    // Remove item from list

})

