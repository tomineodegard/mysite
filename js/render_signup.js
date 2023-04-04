"use strict"

async function render_signup() {
    const form = event.target.form;
    const connection = await fetch("/api-signup", {
     method: "POST",
     body: new FormData(form),
    });

    const data = await connection.json();
    data.info === "success signup" ? location.href = `/` : displayError
    console.log(data)

    function displayError() {
        console.log(data.info)
    }
};
   