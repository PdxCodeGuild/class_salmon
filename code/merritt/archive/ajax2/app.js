let target = document.getElementById("target");
let getQuoteButton = document.getElementById("quote-button");
let quoteField = document.getElementById("quote-field");

function getQuote(e) {
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
      console.log(req.responseText);
      let response = JSON.parse(req.responseText);
      console.log(response);
      
      target.innerHTML = "";
      response.quotes.forEach(function(quote) {
        let resultHTML = `
            <p>${quote.body}</p>
            <p><i><a href="${quote.url}">${quote.author}</a></i></p>
            `
        let newdiv = document.createElement("div");
        newdiv.className = "item";
        newdiv.innerHTML = resultHTML;
        target.appendChild(newdiv)
      });
  });

  let url = `https://favqs.com/api/quotes?filter=${encodeURIComponent(quoteField.value)}`;

  req.open("GET", url);
  req.setRequestHeader("Authorization", 'Token token="4b3888849b4ef0bec9f217ffd39869a9"');
  req.send()
}

quoteField.addEventListener("keydown", function(e) {
  if (e.keyCode === 13) {
    getQuote(e);
  }; 
});

getQuoteButton.addEventListener("click", getQuote);

