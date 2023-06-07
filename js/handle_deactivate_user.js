"use strict"

async function handleDeactivateUser() {
    const form = event.target
    console.log(form)

    const connection = await fetch(`/api-deactivate-user`, {
        method: "POST",
        body: new FormData(form)
    })
    
    const data = await connection.json()
    console.log(data)


    document.querySelector("#deactivate_form").innerHTML =
    `
    <form class="flex flex-col mt-8" >
        <input type="text" name="user_id" id="user_id" value="{{cookie_user['user_id']}}" style="display:none">
        <button class="cursor-pointer border border-twitterRed py-2 px-6 rounded-full text-twitterRed flex justify-center">Please check your email</button>
    </form>
    `

};