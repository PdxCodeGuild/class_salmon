let conversion_dict = {
    " ": ' ',
    A: 'N',
    a: 'n',
    B: 'O',
    b: 'o',
    C: 'P',
    c: 'p',
    D: 'Q',
    d: 'q',
    E: 'R',
    e: 'r',
    F: 'S',
    f: 's',
    G: 'T',
    g: 't',
    H: 'U',
    h: 'u',
    I: 'V',
    i: 'v',
    J: 'W',
    j: 'w',
    K: 'X',
    k: 'x',
    L: 'Y',
    l: 'y',
    M: 'Z',
    m: 'z',
    N: 'A',
    n: 'a',
    O: 'B',
    o: 'b',
    P: 'C',
    p: 'c',
    Q: 'D',
    q: 'd',
    R: 'E',
    r: 'e',
    S: 'F',
    s: 'f',
    T: 'G',
    t: 'g',
    U: 'H',
    u: 'h',
    V: 'I',
    v: 'i',
    W: 'J',
    w: 'j',
    X: 'K',
    x: 'k',
    Y: 'L',
    y: 'l',
    Z: 'M',
    z: 'm'
}



// msg = prompt("Enter a message to encrypt: ")

// let output = '';
// let word = [];
// // let ords =[];
// for (char of msg) {
//     // console.log(char)
//     // console.log(char.charCodeAt(0))
//     word.push(char)
// }
// // console.log(word)

// for (char of word) {
//     output += conversion_dict[char]
// }
// alert(`${output}`)
// console.log(output)

let body = document.getElementById("body");

let form = document.createElement('form');
    form.action = "";
    form.method = "post";

body.appendChild(form);

let msg = document.createElement('input');
    msg.type = "text";
    msg.id = "msg";
    msg.placeholder = "Enter message to encrypt"

form.appendChild(msg);

let submit_btn = document.createElement('input');
    submit_btn.type = "submit"
    submit_btn.value = "Encrypt"

form.appendChild(submit_btn);

let results = document.createElement('h4')
    results.id = "result"
    results.innerText = ''

body.appendChild(results);

submit_btn.addEventListener('click', function(event) {
    event.preventDefault()
    let message = document.getElementById("msg")
    let msg = message.value
    let output = ""
    for (char of msg) {
        output += conversion_dict[char]
    }
    results.innerText = output
    
    // console.log(output)
})