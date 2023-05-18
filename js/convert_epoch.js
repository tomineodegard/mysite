"use strict"

window.addEventListener("load", timestamps); 


function timestamps() { 
    const epoch = document.querySelectorAll(".epoch"); 
    epoch.forEach((e) => { 
        const epochTimestamp = Number(e.textContent); 
        // console.log(e.textContent);

        // console.log(epochTimestamp);

        const date = new Date(epochTimestamp * 1000); 
        const dateOptions = { 
            // day: "numeric", 
            month: "long", 
            year: "numeric",
        }; 
        const created_at = new Intl.DateTimeFormat("en-GB", dateOptions).format(date); 
        e.textContent = created_at; 
    }); 
}