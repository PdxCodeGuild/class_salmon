let target = document.getElementById("target");
let btn = document.getElementById("btn-dog");

btn.addEventListener("click", function(e) {
  let req = new XMLHttpRequest();

  req.addEventListener("progress", function(e) {
    target.innerText = `Request ${ e.loaded / e.total * 100 }% complete.`
  });

  req.addEventListener("error", function(e) {
    target.innerText = `${req.statusText} ${req.status}`
    console.log(req);
  });

  req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    console.log(response);
  });

  req.open("GET", 'https://favqs.com/api/quotes?filter=dog');
  req.setRequestHeader("Authorization", 'Token token="4b3888849b4ef0bec9f217ffd39869a9"');
  req.send()
});