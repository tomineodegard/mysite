"use strict"

async function handleDeactivateUser() {
    console.log("I am inside handleDeactivateUser.js")

    const form = event.target
    console.log(form)

    const connection = await fetch(`/api-request-deactivate-user-key`, {
        method: "POST",
        body: new FormData(form)
    })
    
    const data = await connection.json()
    console.log(data)

};

async function handleConfirmDeactivateUser() {
    console.log("I am inside handleConfirmDeactivateUser.js")

    const form = event.target
    console.log(form)
    console.log(form.user_deactivate_key1.value)

    const connection = await fetch(`/api-deactivate-user/${form.user_deactivate_key1.value}`, {
        method: "GET"
    })
    const data = await connection.json()
    console.log(data)

};