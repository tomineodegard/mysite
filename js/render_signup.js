"use strict"

async function render_signup() {
    const form = event.target;
    console.log(form);
    const connection = await fetch("/api-signup", {
     method: "POST",
     body: new FormData(form),
    });

    const data = await connection.json();
    data.info === "Your new user has been created. However, before you can log in, you need to check your email to validate your identity." ? displaySuccess() : displayError()
    console.log(data)


    function displaySuccess() {
        const successMessage = data.info;
        console.log(successMessage)
        document.querySelector("#modal_success_signup").classList.remove("hidden");
        document.querySelector("#successMessage").textContent = successMessage
    };


    function displayError() {
        const errorMessage = data.info;
        console.log(errorMessage)

        document.querySelector("#modal_error").classList.remove("hidden");
        document.querySelector("#errorMessage").textContent = errorMessage
    }
};

function closeModalError() {
    document.querySelector("#modal_error").classList.add("hidden");
};

function closeModalSuccess() {
    document.querySelector("#modal_success_signup").classList.add("hidden");
};
   