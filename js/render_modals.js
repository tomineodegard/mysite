"use strict"

// profile options in comp left
function toggleModalProfileOptions() {
    document.querySelector("#modal_profile_options").classList.toggle("hidden");
};

// settings on cookie_users profile page
function displayModalSettings() {
    document.querySelector("#modal_settings").classList.remove("hidden");
};

function closeModalSettings() {
    document.querySelector("#modal_settings").classList.add("hidden");
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