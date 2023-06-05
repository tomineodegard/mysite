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

    if (conn.ok) {
        console.log("ok")
    } else {
        console.log("error")
    }

    const el = frm.parentElement;
    el.closest("article").remove()
};
   