"use strict"

async function follow(){
    const frm = event.target
    const cookie_user_profile = document.querySelector("#cookie_user_profile")
    const follow_unfollow_container = document.querySelector("#follow_unfollow")

    const conn = await fetch("/api-follow", {
        method : "POST",
        body : new FormData(frm)
        
    })

    const data = await conn.json()
    
    data.user_total_followers === 3 ?
    document.querySelectorAll("#verified_container").forEach((e) => {
        e.insertAdjacentHTML("beforeend", 
        `<svg id="verified_icon" xmlns="http://www.w3.org/2000/svg" class="text-twitterBlue" width="20" height="20" viewBox="0 0 24 24">
            <g fill="none">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M10.054 2.344a3 3 0 0 1 3.892 0l1.271 1.084a1 1 0 0 0 .57.236l1.665.133a3 3 0 0 1 2.751 2.751l.133 1.666a1 1 0 0 0 .236.569l1.084 1.271a3 3 0 0 1 0 3.892l-1.084 1.271a1 1 0 0 0-.236.57l-.133 1.665a3 3 0 0 1-2.751 2.751l-1.666.133a1 1 0 0 0-.569.236l-1.271 1.084a3 3 0 0 1-3.892 0l-1.271-1.084a1 1 0 0 0-.57-.236l-1.665-.133a3 3 0 0 1-2.751-2.751l-.133-1.666a1 1 0 0 0-.236-.569l-1.084-1.271a3 3 0 0 1 0-3.892l1.084-1.271a1 1 0 0 0 .236-.57l.133-1.665a3 3 0 0 1 2.751-2.751l1.666-.133a1 1 0 0 0 .569-.236l1.271-1.084zm5.653 8.363a1 1 0 0 0-1.414-1.414L11 12.586l-1.293-1.293a1 1 0 0 0-1.414 1.414l2 2a1 1 0 0 0 1.414 0l4-4z" fill="currentColor"/>
            </g>
        </svg>`)
    }) : null
    

    const unfollowForm = frm.parentNode.insertAdjacentHTML("beforeend", 
        `<form id="unfollow_form" onsubmit="unfollow(); return false;">
            <input type="text" name="unfollowee_fk" value="${data.followee_fk}" style="display: none" />
            <button type="submit" class="ml-auto px-4 py-2 border border-twitterLightGray bg-transparent ease-in duration-100 hover:border-twitterRed hover:text-twitterRed rounded-full text-sm font-medium before:content-['Following'] hover:before:content-['Unfollow']"></button>
        </form>
        `)

    frm.remove();


    if(cookie_user_profile) {
    document.querySelector("#user_total_following").textContent++;
    } else if (follow_unfollow_container) {
    document.querySelector("#user_total_followers").textContent = data.user_total_followers;
    }
}