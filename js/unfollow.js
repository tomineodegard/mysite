"use strict"

async function unfollow(){
    const frm = event.target
    console.log(frm)
    const username = frm[0].value
    const cookie_user_profile = document.querySelector("#cookie_user_profile")
    const parent = event.target.parentElement.id
    console.log(parent)

    const conn = await fetch("/api-unfollow", {
        method : "DELETE",
        body : new FormData(frm)

    })
    
    const data = await conn.json()
    console.log(data)
    console.log(`ok unfollow ${username}`)


    frm.remove();
    document.querySelector(`#${parent}`).insertAdjacentHTML(
        "afterbegin",
        `
        <form onsubmit="follow(); return false">
            <input type="text" name="followee_fk" value="${username}" style="display:none">
            <button class="ml-auto px-4 py-2 text-black text-base font-medium bg-gray-200 rounded-full">Follow</button>
        </form>  
        `
    )

    const decrement_user_followers = document.querySelector("#user_total_followers");
    const decrement_my_following = document.querySelector("#my_total_following");

    
    if(cookie_user_profile) {
        console.log("true")
    } else if(decrement_user_followers) {
        decrement_user_followers.textContent--
    }

    if(cookie_user_profile) {
        decrement_my_following.textContent--
    } else {
        console.log("false")
    }

}