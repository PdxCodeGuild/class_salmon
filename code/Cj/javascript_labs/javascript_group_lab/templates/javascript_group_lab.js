
body = document.getElementById("body");

let form = document.createElement('form');
    form.method = "post";
    form.action = '';

body.appendChild(form)

let forminput = document.createElement('input');
    forminput.type = "text"
    forminput.id = "thing"
form.appendChild(forminput);

let submit_btn = document.createElement('input');
    submit_btn.type = 'submit';
    submit_btn.value = 'Add item';

form.appendChild(submit_btn);


let div1 = document.createElement('div');
    div1.id = 'div1';
body.appendChild(div1);


let todo_ul = document.createElement('ul');
todo_ul.id = "todo";
div1.appendChild(todo_ul);

let todo = document.createElement('h4');
todo.innerText = "To do list: ";
todo_ul.appendChild(todo);


let div2 = document.createElement('div');
    div2.id = "div2";

body.appendChild(div2);

let complete = document.createElement('h4');
    complete.innerText = "Completed Tasks: "
div2.appendChild(complete)

let done_ul = document.createElement('ul');
    done_ul.id = 'done-ul'
div2.appendChild(done_ul)

submit_btn.addEventListener('click', function(event) {
    event.preventDefault()
    let data = document.getElementById('thing')
    let li = document.createElement('li');
    li.innerText = data.value;
    li.id = data.value;
    data.value = ''
    
    let check = document.createElement('input');
        check.type = "checkbox"
        check.id = 'check'
        check.name = "checkbox"
    li.appendChild(check);
    // li.appendChild(done_btn);
    todo_ul.appendChild(li);
})

let done_btn = document.createElement('input');
        done_btn.type = 'submit';
        done_btn.value = 'Done';
div1.appendChild(done_btn);



done_btn.addEventListener('click', function(event) {
    event.preventDefault()

    let done_list = document.getElementById('todo');
    let items = done_list.getElementsByTagName('li');
    // console.log(checkbox.checked);
    // console.log(items)
    let checkbox
    // console.log(items);
    var remove_list = []
    for (item of items) {
        // console.log(item)
        checkbox = item.querySelector("input[name=checkbox]");
        // console.log(checkbox.checked)
        if (checkbox.checked) {
            let new_li = document.createElement('li');
            new_li.innerText = item.innerText;
            done_ul.appendChild(new_li);
            // console.log(item);
            remove_list.push(item);
            // todo_ul.removeChild(item);
            // console.log(item.innerText)
        }
    }
    for (i=0; i <= remove_list.length-1; i++) {
        // console.log(remove_list);
        todo_ul.removeChild(remove_list[i]);
    }
// console.log(remove_list)
   
})
let erase_btn = document.createElement('input');
        erase_btn.type = 'submit';
        erase_btn.value = 'Erase';
        
div1.appendChild(erase_btn);
erase_btn.addEventListener('click', function(event) {
    event.preventDefault()

    let erase_list = document.getElementById('todo');
    let items = erase_list.getElementsByTagName('li');
    // console.log(checkbox.checked);
    // console.log(items)
    let checkbox
    // console.log(items);
    var remove_list = []
    for (item of items) {
        // console.log(item)
        checkbox = item.querySelector("input[name=checkbox]");
        // console.log(checkbox.checked)
        if (checkbox.checked) {

            remove_list.push(item); //
            // todo_ul.removeChild(item);
            // console.log(item.innerText)
        }
    }
    for (i=0; i <= remove_list.length-1; i++) {
        // console.log(remove_list);
        todo_ul.removeChild(remove_list[i]);
    }
// console.log(remove_list)
   
})

let clear_btn = document.createElement('input');
        clear_btn.type = 'submit';
        clear_btn.value = 'Clear';
        
div2.appendChild(clear_btn);
clear_btn.addEventListener('click', function(event) {
    event.preventDefault()

    let clear_list = document.getElementById('done-ul');
    let items = clear_list.getElementsByTagName('li');
    let remove_list = []
    for (item of items) {
        console.log(items);
        remove_list.push(item);
    }
   
    for (i=0; i <= items.length-1; i++) {
        // console.log(remove_list);
        clear_list.innerHTML='';
    }
// console.log(remove_list)
   
})
