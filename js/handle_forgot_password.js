"use strict"

async function handleForgotPassword() {
    console.log("i am here - handleForgotPassword")

    const form = event.target;
    console.log(form);
    const connection = await fetch("/api-forgot-password", {
     method: "POST",
     body: new FormData(form),
    });

    const data = await connection.json();
    data.info === "password reset" ? location.href = `login` : displayError();
    console.log(data)

    function displayError() {
        const errorMessage = data.info;
        console.log(errorMessage)

        document.querySelector("#errorModal").classList.remove("hidden");
        document.querySelector("#errorMessage").textContent = errorMessage
    }

};
   