let quoteButton = document.getElementById("quote-button");
let target = document.getElementById("target");

quoteButton.addEventListener('click', function(e) {
  axios({
    url: 'https://favqs.com/api/qotd',
    method: 'get',
    headers: {
      Authorization: 'Token token="4b3888849b4ef0bec9f217ffd39869a9"'
    }
  })
  .then(function(response) {
    console.log(response);
    let resultHTML = `
      <h4>${response.data.quote.body}</h4>
      <p><em><a href=${response.data.quote.url}>${response.data.quote.author}</a></em></p>
    `;
    target.innerHTML = resultHTML;
  })
  .catch(function(error) {
    console.log(error);
  });
});