
function show_search_results() {
    document.getElementById('resultField').classList.remove("hidden");
}

function hide_search_results() {
    document.getElementById('resultField').classList.add("hidden");
}

let the_timer;

async function search() {
    clearTimeout(the_timer);
    the_timer = setTimeout(async function() {

    const user_search_input = document.querySelector("#searchInput").value;

    try {
    const conn = await fetch("/api-search", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({search_input: user_search_input })
    });

    if (conn.ok) {
    const data = JSON.parse(await conn.text());
    const results = data.map((user) => ({
        username: user.username,
        user_profile_picture: user.user_profile_picture
    }));
    
    const searchResults = document.querySelector("#resultField");
    searchResults.innerHTML = "";

    data.forEach((user) => {
        const resultItem = `<a class="font-medium" href="/${user.username}">
                                <div class="cursor-pointer flex gap-2 users-center p-4 hover:bg-twitterDarkGray rounded-full">
                                    <img class="w-12 h-12 rounded-full object-cover" src="/images/profilepictures/${user.user_profile_picture}" alt="">@${user.username}
                                </div>
                            </a>`;
        searchResults.insertAdjacentHTML('beforeend', resultItem);
    });

} else {
    console.error(`Response not OK: ${conn.status}`);
}

} catch (error) {
console.error(error);
}
}, 500);
}