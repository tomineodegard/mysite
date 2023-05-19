"use strict"

async function follow(){
    const frm = event.target
    const username = frm[0].value
    const cookie_user_profile = document.querySelector("#cookie_user_profile")
    const profile = document.querySelector("#profile")

    const parent = event.target.parentElement.id
    console.log(parent)


    const conn = await fetch("/api-follow", {
        method : "POST",
        body : new FormData(frm)
        
    })

    const data = await conn.json()
    
    console.log(data)
    console.log(frm[0].value)
    console.log(`ok follow ${username}`)
    console.log(frm)
    
    document.querySelector(`#${parent}`).insertAdjacentHTML(
        "afterbegin",
        `
        <form onsubmit="unfollow(); return false">
        <input type="text" name="unfollowee_fk" value="${username}" style="display:none">
        <button class="ml-auto px-4 py-2 text-white text-base font-medium border border-white rounded-full">Unfollow</button>
        </form>        `
        )
        
    frm.remove();
    
    const increment_followers = document.querySelector("#user_total_followers");
    const increment_my_following = document.querySelector("#my_total_following");

    if(cookie_user_profile) {
        console.log("true")
    } else if(increment_followers) {
        increment_followers.textContent++
    }


    if(cookie_user_profile) {
        increment_my_following.textContent++
    } else if(increment_my_following) {
        console.log("true")
    }

}
