


function sendCommandToStore(store, cmd) {
  document.getElementById("demo").innerHTML = "Paragraph changed.";

  //fetch('http://localhost:5000/store/1/0')
  //.then(response => response.json())
  //.then(data => console.log(data));

  var pathToBackEnd = "http://localhost:5000/store/"
  //fetch(pathToBackEnd + String(store) + "/" + String(cmd));


  postData(pathToBackEnd + String(store) + "/" + String(cmd), { answer: 42 })
  .then(data => {
    console.log(data); // JSON data parsed by `data.json()` call
  });
}


// Example POST method implementation:
async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  });
  return response.json(); // parses JSON response into native JavaScript objects
}


