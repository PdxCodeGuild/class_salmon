// '''
// A simple JSON-based database that can be used with Flask.
// Usage:
​
// import from jsondb import JsonDB
// db = JsonDB('database.json')
// db.load()
// x = db.get('x', 0)
// x += 1
// db.set('x', x)
// db.save()
// '''
​
​
// import json
​
​
// class JsonDB:
//     def __init__(self, path='db.json'):
//         self.path = path
//         self.data = None
​
//     def load(self):
//         with open(self.path, 'r') as file:
//             self.data = json.loads(file.read())
​
//     def save(self):
//         with open(self.path, 'w') as file:
//             file.write(json.dumps(self.data, indent=4, sort_keys=True))
​
//     def __getitem__(self, key):
//         return self.data[key]
​
//     def __setitem__(self, key, value):
//         self.data[key] = value
​
//     def __delitem__(self, key):
//         del self.data[key]
​
//     def get(self, key, default=None):
//         return self.data.get(key, default)
​
//     def set(self, key, value):
//         self.data[key] = value
​
//     def clear(self, key=None):
//         if key is not None:
//             del self.data[key]
//         else:
//             self.data = {}
​
let todo = {
​
}
​
body = document.getElementById("body");
​
let form = document.createElement('form');
    form.method = "post";
    form.action = '';
​
body.appendChild(form)
​
let forminput = document.createElement('input');
    forminput.type = "text"
    forminput.id = "thing"
form.appendChild(forminput);
​
let submit_btn = document.createElement('input');
    submit_btn.type = 'submit';
    submit_btn.value = 'Add item';
​
form.appendChild(submit_btn)
​
let ul = document.createElement('ul');
​
form.appendChild(ul)
​
submit_btn.addEventListener('click', function(event) {
    event.preventDefault()
    let data = document.getElementById('thing')
    let li = document.createElement('li');
    li.innerText = data.value
    let done_btn = document.createElement('input');
        done_btn.type = 'submit';
        done_btn.value = 'Done';
​
    li.appendChild(done_btn);
    ul.appendChild(li);
})
​
done_btn.addEventListener('click', function(event) {
    
})
​
// function additem(item) {
    
// }