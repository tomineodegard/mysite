async function post(){
    const frm = event.target // the form
    const conn = await fetch("/post", {
        method: "POST",
        body:  new FormData(frm)
    })
    // const data = await conn.text() // to get plain text
    const postData = await conn.json() // to get plain text
    console.log(postData)

    if (!conn.ok){
        console.log("Cannot post")
        showTip(postData.info)        
        return
    }

    let postImageDataSaved;
    if (frm.post_image.files.length) {
        let formData = new FormData(frm);
        formData.append("post_id", postData.post_id)

        const postImageConn = await fetch("/upload-post-image", {
            method: "POST",
            body: formData
        })
        const postImageData = await postImageConn.json()
        console.log(postImageData)
        postImageDataSaved = postImageData
    }

    if (!postImageDataSaved) {
        postImageDataSaved = "";
    } 

    // const message = frm.querySelector("input[name='message']").value
    let user_verified = postData.user.user_verified
    if (postData.user.user_verified == "0") {
        user_verified = "";
    }
    
    const posts = document.querySelector("#posts").insertAdjacentHTML("afterbegin", 
    `<div class="flex w-full border-t border-gray-600 overflow-hidden">
        <a href="/${postData.user.user_username}" class="p-4 flex flex-col justify-between">
            <img src="/assets/images/avatars/${postData.user.user_avatar}" class="w-16 min-w-[3rem] rounded-full" alt="" />
        </a>
        <div class="w-full pr-4 pt-4">
            <div>
                <div class="flex flex-col">
                    <p class="flex w-full">
                    <div>
                        <a href="/${postData.user.user_username}" class="font-semibold text-slate-200 text-base hover:underline underline-offset-2 pr-1">
                            ${postData.user.user_first_name} ${postData.user.user_last_name}
                        </a>
                    </div>
                    <div>
                    ${user_verified &&
                        `<a href="/${postData.user.user_username}" class="flex items-center">
                            <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-label="Verified account" role="img" class="" data-icon-verified="icon-verified" width="20" height="20">
                                <g fill="#1D9BF0">
                                    <path d="M22.25 12c0-1.43-.88-2.67-2.19-3.34.46-1.39.2-2.9-.81-3.91s-2.52-1.27-3.91-.81c-.66-1.31-1.91-2.19-3.34-2.19s-2.67.88-3.33 2.19c-1.4-.46-2.91-.2-3.92.81s-1.26 2.52-.8 3.91c-1.31.67-2.2 1.91-2.2 3.34s.89 2.67 2.2 3.34c-.46 1.39-.21 2.9.8 3.91s2.52 1.26 3.91.81c.67 1.31 1.91 2.19 3.34 2.19s2.68-.88 3.34-2.19c1.39.45 2.9.2 3.91-.81s1.27-2.52.81-3.91c1.31-.67 2.19-1.91 2.19-3.34zm-11.71 4.2L6.8 12.46l1.41-1.42 2.26 2.26 4.8-5.23 1.47 1.36-6.2 6.77z" fill="#1D9BF0"></path>
                                </g>
                            </svg>
                        </a>`
                        }
                    </div>
                    
                    <a href="/${postData.user.user_username}" class="text-sm flex items-center text-gray-500 pl-1">
                        <strong>@</strong>${postData.user.user_username}
                    </a>
                    <a href="/${postData.user.user_username}" class="text-sm flex items-center text-gray-500 pl-1">
                        Â·&nbsp;<span class="post_created_at">Just now</span>
                    </a>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
                        class="w-6 h-6 ml-auto text-zinc-400 hover:text-sky-600 hover:cursor-pointer">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z"/>
                    </svg>
                    </p>
                    <div class="flex flex-col text-base">
                        <p class="break-words break-all">${postData.post_message}</p>
                        ${postImageDataSaved &&
                        `<img src="/assets/images/post_images/${postImageDataSaved.post_image}" class="rounded-xl mt-4" alt="" />`
                        }
                    </div>
                </div>

                <div class="flex justify-between mt-4 text-gray-700 pr-6 pb-6">
                    <div class="flex items-center cursor-pointer group">
                        <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
                            <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"
                            class="fill-gray-500 group-hover:fill-[#1D9BF0] transition ease-in-out" width="20" height="20">
                                <g>
                                    <path d="M1.751 10c0-4.42 3.584-8 8.005-8h4.366c4.49 0 8.129 3.64 8.129 8.13 0 2.96-1.607 5.68-4.196 7.11l-8.054 4.46v-3.69h-.067c-4.49.1-8.183-3.51-8.183-8.01zm8.005-6c-3.317 0-6.005 2.69-6.005 6 0 3.37 2.77 6.08 6.138 6.01l.351-.01h1.761v2.3l5.087-2.81c1.951-1.08 3.163-3.13 3.163-5.36 0-3.39-2.744-6.13-6.129-6.13H9.756z"></path>
                                </g>
                            </svg>
                        </span>
                        <span data-abbreviate-num="post_total_replies" class="text-sm text-gray-500 group-hover:text-[#1D9BF0] transition ease-in-out">${postData.post_total_replies}</span>
                    </div>
                    <div class="flex items-center cursor-pointer group">
                        <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
                            <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"
                            class="fill-gray-500 group-hover:fill-emerald-500 transition ease-in-out" width="20" height="20">
                                <g>
                                    <path d="M4.75 3.79l4.603 4.3-1.706 1.82L6 8.38v7.37c0 .97.784 1.75 1.75 1.75H13V20H7.75c-2.347 0-4.25-1.9-4.25-4.25V8.38L1.853 9.91.147 8.09l4.603-4.3zm11.5 2.71H11V4h5.25c2.347 0 4.25 1.9 4.25 4.25v7.37l1.647-1.53 1.706 1.82-4.603 4.3-4.603-4.3 1.706-1.82L18 15.62V8.25c0-.97-.784-1.75-1.75-1.75z"></path>
                                </g>
                            </svg>
                        </span>
                        <span data-abbreviate-num="post_total_reposts" class="text-sm text-gray-500 group-hover:text-emerald-500 transition ease-in-out">${postData.post_total_reposts}</span>
                    </div>
                    <div class="flex items-center hover cursor-pointer group">
                        <span class="group-hover:bg-pink-600/[0.15] transition ease-in-out rounded-full p-2">
                            <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"
                            class="fill-gray-500 group-hover:fill-pink-600 transition ease-in-out r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi" width="20" height="20">
                                <g>
                                    <path d="M16.697 5.5c-1.222-.06-2.679.51-3.89 2.16l-.805 1.09-.806-1.09C9.984 6.01 8.526 5.44 7.304 5.5c-1.243.07-2.349.78-2.91 1.91-.552 1.12-.633 2.78.479 4.82 1.074 1.97 3.257 4.27 7.129 6.61 3.87-2.34 6.052-4.64 7.126-6.61 1.111-2.04 1.03-3.7.477-4.82-.561-1.13-1.666-1.84-2.908-1.91zm4.187 7.69c-1.351 2.48-4.001 5.12-8.379 7.67l-.503.3-.504-.3c-4.379-2.55-7.029-5.19-8.382-7.67-1.36-2.5-1.41-4.86-.514-6.67.887-1.79 2.647-2.91 4.601-3.01 1.651-.09 3.368.56 4.798 2.01 1.429-1.45 3.146-2.1 4.796-2.01 1.954.1 3.714 1.22 4.601 3.01.896 1.81.846 4.17-.514 6.67z"></path>
                                </g>
                            </svg>
                        </span>
                        <span data-abbreviate-num="post_total_likes" class="text-sm text-gray-500 group-hover:text-pink-600 transition ease-in-out">${postData.post_total_likes}</span>
                    </div>
                    <div class="hidden lg:flex items-center cursor-pointer group">
                        <span
                            class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
                            <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"strok aria-hidden="true"
                            class="fill-gray-500 group-hover:fill-[#1D9BF0] transition ease-in-out" width="20" height="20">
                                <g>
                                    <path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.004-10h2L6 21H4zm9.248 0v-7h2v7h-2z"></path>
                                </g>
                            </svg>
                        </span>
                        <span data-abbreviate-num="post_total_views" class="pl-2 text-sm text-gray-500 group-hover:text-[#1D9BF0] transition ease-in-out">${postData.post_total_views}</span>
                    </div>
                    <div class="flex items-center cursor-pointer group">
                        <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
                            <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"
                            class="fill-gray-500 group-hover:fill-[#1D9BF0] transition ease-in-out r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi" width="20" height="20">
                                <g>
                                    <pathd="M12 2.59l5.7 5.7-1.41 1.42L13 6.41V16h-2V6.41l-3.3 3.3-1.41-1.42L12 2.59zM21 15l-.02 3.51c0 1.38-1.12 2.49-2.5 2.49H5.5C4.11 21 3 19.88 3 18.5V15h2v3.5c0 .28.22.5.5.5h12.98c.28 0 .5-.22.5-.5L19 15h2z"></pathd=>
                                </g>
                            </svg>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>`)
}

function previewpostImg() {
    const post_image_preview = document.querySelectorAll(".post_image_preview")
    const post_image_input = document.querySelectorAll(".post_image_upload")

    Object.values(post_image_input).forEach((e, i) => {
        const post_image = post_image_input[i].files
        
        if (post_image.length) {
            // if (e.id === "post_image_modal") {    
            //     post_image_input[1].files = post_image[i]
            // }
            // if (e.id === "post_image_index") {    
            //     post_image_input[0].files = post_image[i]
            // }

            post_image_preview[i].src = URL.createObjectURL(post_image[0])

            if (e.id === "post_image_modal") {
                const postModalDialog = document.querySelector("[data-post-modal=post_modal_dialog]")
                postModalDialog.classList.replace("sm:top-[30%]", "sm:top-[50%]")
            }
        }
    })
}