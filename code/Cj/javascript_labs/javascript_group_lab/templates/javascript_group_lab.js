
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
    data.value = '';
    
    let check = document.createElement('input');
        check.type = "checkbox"
        check.id = 'check'
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
    let todo_ul = document.getElementById('todo');
    console.log(todo_ul)
    for (li in todo_ul) {
        console.log(li)
        if (document.getElementById('check').checked) {
            done_ul.appendChild(li);
            todo_ul.removeChild(li);
        }
    }
   
})