"use strict"

async function handleAdminDeleteUser() {
    console.log("i am here - handleAdminDeleteUser")

    const frm = event.target
    const conn = await fetch(`/api-admin-delete-user`, {
        method: "DELETE",
        body: new FormData(frm)
    })

    const data = await conn.json();
    console.log(data)

    document.querySelector("#admin_delete_user_form").innerHTML = `
    <form class="flex justify-between gap-4">
        <input type="text" name="user_id" value="{{user['user_id']}}" style="display:none">
        <button type="submit" class="ml-auto px-4 py-2 text-twitterLightGray text-sm font-medium border border-twitterDarkGray rounded-full opacity-40">User is deleted</button>
    </form>`

    if (conn.ok) {
        console.log("ok")
    } else {
        console.log("error")
    }

    // const el = frm.parentElement;
    // el.closest("article").remove()
};
   