"use strict"

async function render_login() {
    const frm = event.target;
   
    const conn = await fetch("/api-login", {
     method: "POST",
     body: new FormData(frm),
    })
    const data = await conn.json();
    data.info === "success login" ? location.href = `/` : displayError
    console.log(data)


    function displayError() {
        console.log(data.info)
    }
};

