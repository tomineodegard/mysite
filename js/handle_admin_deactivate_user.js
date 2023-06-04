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

    frm.insertAdjacentHTML(
        "beforebegin",
        `
        <form onsubmit="handleAdminActivateUser(); return false" class="flex justify-between gap-4">
            <input type="text" name="user_id" value="${user_id}" style="display:none">
            <button type="submit" class="ml-auto px-4 py-2 text-white text-sm font-medium border border-white rounded-full">Activate</button>
        </form>
        `
        )

    frm.remove();
    console.log(`${user_id} is deactivated successfully`)
};