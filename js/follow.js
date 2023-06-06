"use strict"

async function follow(){
    const frm = event.target
    // const parent = event.target.parentElement.id
    // console.log(parent)

    const conn = await fetch("/api-follow", {
        method : "POST",
        body : new FormData(frm)
        
    })

    const data = await conn.json()
    console.log(data)
    

    if (document.querySelector("#user_total_followers")) {
        document.querySelector("#user_total_followers").textContent = data.user_total_followers;
    }
   
    console.log("#user_total_followers")
    console.log(document.querySelector("#user_total_followers"))

    
    data.user_total_followers === 3 ?
    document.querySelectorAll("#verified-container").forEach((e) => {
        e.insertAdjacentHTML("beforeend", 
        `<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-label="Verified account" role="img" class="w-5" data-icon-verified="icon-verified">
            <g fill="#1D9BF0">
                <path d="M22.25 12c0-1.43-.88-2.67-2.19-3.34.46-1.39.2-2.9-.81-3.91s-2.52-1.27-3.91-.81c-.66-1.31-1.91-2.19-3.34-2.19s-2.67.88-3.33 2.19c-1.4-.46-2.91-.2-3.92.81s-1.26 2.52-.8 3.91c-1.31.67-2.2 1.91-2.2 3.34s.89 2.67 2.2 3.34c-.46 1.39-.21 2.9.8 3.91s2.52 1.26 3.91.81c.67 1.31 1.91 2.19 3.34 2.19s2.68-.88 3.34-2.19c1.39.45 2.9.2 3.91-.81s1.27-2.52.81-3.91c1.31-.67 2.19-1.91 2.19-3.34zm-11.71 4.2L6.8 12.46l1.41-1.42 2.26 2.26 4.8-5.23 1.47 1.36-6.2 6.77z" fill="#1D9BF0"></path>
            </g>
        </svg>`)
    }) : null
    

    const unfollowForm = frm.parentNode.insertAdjacentHTML("beforeend", 
        `<form id="unfollow_form" onsubmit="unfollow(); return false;">
            <input type="text" name="unfollowee_fk" value="${data.followee_fk}" style="display: none" />
            <button type="submit" class="ml-auto px-4 py-2 border border-twitterLightGray bg-transparent ease-in duration-100 hover:border-twitterRed hover:text-twitterRed rounded-full text-sm font-medium before:content-['Following'] hover:before:content-['Unfollow'] w-28"></button>
        </form>
        `)

    frm.remove();
}