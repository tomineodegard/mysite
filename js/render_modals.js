"use strict"

// profile options in comp left
function toggleModalProfileOptions() {
    document.querySelector("#modal_profile_options").classList.toggle("hidden");
};

// edit profile on cookie_users page
function displayModalEditProfile() {
    console.log("displayEditProfile")
    document.querySelector("#modal_edit_profile").classList.remove("hidden");
};

function closeModalEditProfile() {
    document.querySelector("#modal_edit_profile").classList.add("hidden");
};


// delete tweet full screen modal
function displayModalDeleteTweet() {
    document.querySelector("#modal_delete_tweet").classList.remove("hidden");
};

function closeModalDeleteTweet() {
    document.querySelector("#modal_delete_tweet").classList.add("hidden");
};


// delete user full screen modal
function displayModalDeleteUser() {
    document.querySelector("#modal_delete_user").classList.remove("hidden");
};

function closeModalDeleteUser() {
    document.querySelector("#modal_delete_user").classList.add("hidden");
};