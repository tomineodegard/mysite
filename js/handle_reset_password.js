"use strict"

async function handleResetPassword() {
    console.log("i am here - handleResetPassword")

    const form = event.target;
    console.log(form);
    const connection = await fetch("/api-reset-password", {
     method: "POST",
     body: new FormData(form),
    });

    const data = await connection.json();
    console.log(data)

    if (connection.ok) {
        location.href = "/login"
    } else {
            const errorMessage = data.info;
            console.log(errorMessage)
    
            document.querySelector("#errorModal").classList.remove("hidden");
            document.querySelector("#errorMessage").textContent = errorMessage
    }
};
   