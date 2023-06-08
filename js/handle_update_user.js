"use strict"

async function handleUpdateUser() {
    const frm = event.target
    const conn = await fetch("/api-update-user", {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)

    // console.log(user_cover_picture_upload)
    // console.log(user_cover_picture_upload.files.length)
    
    
    
    if (user_profile_picture_upload.files.length) {
        const connToProfilePicture = await fetch("/api-update-user-profile-picture", {
            method: "POST",
            body: new FormData(frm)
        })
        const dataToProfilePicture = await connToProfilePicture.json()
        console.log(dataToProfilePicture)
    }
    
    if (user_cover_picture_upload.files.length) {
        const connToCoverPic = await fetch("/api-update-user-cover-picture", {
            method: "POST",
            body: new FormData(frm)
            
        })
        
        const dataToCoverPic = await connToCoverPic.json()
        console.log(dataToCoverPic)
    }
}

function previewImg() {
    const [coverpicture] = user_cover_picture_upload.files;
    const [profilepicture] = user_profile_picture_upload.files;

    if (coverpicture) user_cover_picture_preview.src = URL.createObjectURL(coverpicture)
    if (profilepicture) user_profile_picture_preview.src = URL.createObjectURL(profilepicture)
}