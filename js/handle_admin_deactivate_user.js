"use strict"

async function handleAdminDeactivateUser() {
    const frm = event.target
    console.log(frm)
    const user_id = frm[0].value
    const parent = event.target.parentElement.id
    console.log(parent)

    const conn = await fetch(`/api-admin-deactivate-user`, {
        method: "POST",
        body: new FormData(frm)
    })
    
    const data = await conn.json()
    console.log(data)

    document.querySelector(`#${parent}`).insertAdjacentHTML(
        "afterbegin",
        `
        <form onsubmit="handleAdminDeactivateUser(); return false" class="flex justify-between gap-4">
            <input type="text" name="user_id" value="${user_id}" style="display:none">
            <button type="submit" class="ml-auto px-4 py-2 text-white text-sm font-medium border border-twitterGreen rounded-full">Activate</button>
        </form>
        `
        )

    frm.remove();
    console.log(`${user_id} is deactivated successfully`)
};