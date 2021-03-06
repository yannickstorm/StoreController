


function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";

  fetch('localhost:5000/store/')
  .then(response => response.json())
  .then(data => console.log(data));
}


