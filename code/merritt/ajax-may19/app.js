let target = document.getElementById("target"); // Define the HTML element to update
let getQuoteButton = document.getElementById("quote-button");

getQuoteButton.addEventListener("click", function(e) {
  let req = new XMLHttpRequest();
  
  req.addEventListener("progress", function(e) {
    console.log(e.loaded);
    target.innerText = "Loading...";
  });
  req.addEventListener("error", function(e) {
    console.log(e.status);
    target.innerText = "Cannot load quote. Try again later!";
  });
  req.addEventListener("load", function(e) {
    console.log(req.responseText); // returns the raw text response
    let response = JSON.parse(req.responseText);
    console.log(response); // returns a JavaScript object
  
    let resultHTML = `
    <p>${response.quote.body}</p>
    <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
    `
    target.innerHTML = resultHTML;
  });
  
  req.open("GET", "https://favqs.com/api/qotd");
  req.setRequestHeader("Authorization", 'Token token="4b3888849b4ef0bec9f217ffd39869a9"');
  req.send()
});

