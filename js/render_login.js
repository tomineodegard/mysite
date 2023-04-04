"use strict"

async function render_login() {
    const form = event.target;
    const connection = await fetch("/api-login", {
     method: "POST",
     body: new FormData(form),
    })
    const data = await connection.json();
    data.info === "success login" ? location.href = `/` : displayError
    console.log(data)


    function displayError() {
        console.log(data.info)
    }
};

