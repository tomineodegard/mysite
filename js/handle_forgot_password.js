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
    data.info === "An email is sent, please check your inbox to reset your password." ? displaySuccess() : displayError();

    console.log(data)


    function displaySuccess() {
        const successMessage = data.info;
        console.log(successMessage)
        document.querySelector("#modal_success").classList.remove("hidden");
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
    document.querySelector("#modal_success").classList.add("hidden");
};