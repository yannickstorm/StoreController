


function sendCommandToStore(store, cmd) {
  document.getElementById("demo").innerHTML = "Paragraph changed.";

  //fetch('http://localhost:5000/store/1/0')
  //.then(response => response.json())
  //.then(data => console.log(data));

  var pathToBackEnd = "http://storecontrolstation:5000/store/"
  fetch(pathToBackEnd + String(store) + "/" + String(cmd));
}


