"use strict"

async function handleResetPassword() {
    console.log("i am here")

    const form = event.target;
    console.log(form);
    const connection = await fetch("/api-reset-password-email", {
     method: "POST",
     body: new FormData(form),
    });

    const data = await connection.json();
    location.href = "/reset_password"
};
   