"use strict"

async function follow(){
    const frm = event.target
    // const username = frm[0].value

    const conn = await fetch("/api-follow", {
        method : "POST",
        body : new FormData(frm)
        
    })

    const data = await conn.json()
    
    console.log(data)
    console.log(data.username)


    console.log("ok follow")
    
    console.log(frm)
    frm.remove();
    document.querySelector("#follow_unfollow").insertAdjacentHTML(
        "afterend",
        `
        <form id="" onsubmit="unfollow(); return false">
            <input type="text" name="unfollowee_fk" value="${data.username}" style="display:none">
            <button class="ml-auto px-4 py-2 text-black text-base font-medium bg-gray-200 rounded-full">Unfollow</button>
        </form>        `
    )
}