"use strict"

async function handleUpdateUser() {
    const frm = event.target
    const conn = await fetch("/api-update-user", {
        method : "POST",
        body : new FormData(frm)
        
    })

    const data = await conn.json()
    console.log(data)

};