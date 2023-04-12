"use strict"

async function render_signup() {
    const form = event.target;
    console.log(form);
    const connection = await fetch("/api-signup", {
     method: "POST",
     body: new FormData(form),
    });

    const data = await connection.json();
    data.info === "a new user is created" ? location.href = `/` : displayError()
    console.log(data)

    function displayError() {
        console.log(data.info)
        // TO DO: Create popup with error message
    }
};
   