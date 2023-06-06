"use strict"

async function unfollow(){
    const frm = event.target
    const conn = await fetch("/api-unfollow", {
        method : "DELETE",
        body : new FormData(frm)

    })
    
    const data = await conn.json()
    console.log(data)

    if (document.querySelector("#user_total_followers")) {
        document.querySelector("#user_total_followers").textContent = data.user_total_followers;
    }

    console.log("#user_total_followers")
    console.log(document.querySelector("#user_total_followers"))

    // (!)data.user_is_verified ? document.querySelectorAll("#verified_icon").forEach((e) => {
    //     e.remove()
    // }) : null

    const followForm = frm.parentNode.insertAdjacentHTML("beforeend", 
    `
    <form id="follow_form" onsubmit="follow(); return false;">
        <input type="text" name="followee_fk" value="${data.unfollowee_fk}" style="display: none" />
        <button class="ml-auto px-4 py-2 text-black text-sm font-medium bg-white rounded-full">Follow</button>
    </form>
    `)

    frm.remove();
}