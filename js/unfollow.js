"use strict"

async function unfollow(){
    const frm = event.target
    console.log(frm)

    const conn = await fetch("/api-unfollow", {
        method : "DELETE",
        body : new FormData(frm)

    })
    
    const data = await conn.json()
    console.log(data)
    console.log(data.username)


    console.log("ok unfollow")

    frm.remove();
    document.querySelector("#follow_unfollow").insertAdjacentHTML(
        "afterend",
        `
        <form id="" onsubmit="follow(); return false">
            <input type="text" name="unfollowee_fk" value="${data.username}" style="display:none">
            <button class="ml-auto px-4 py-2 text-black text-base font-medium bg-gray-200 rounded-full">Follow</button>
        </form>  
        `
    )

}