//When the element with id="submit-button" is clicked, send the user an alert message.
//add listener to id submit-button


function addListener() {
    var submitButton = document.getElementById("submit-button");
    submitButton.addEventListener("click", function () {
        alert("You clicked the submit button!");
    });
}

window.onload = addListener;