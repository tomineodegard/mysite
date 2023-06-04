async function handleDeleteTweet() {
    
    const frm = event.target
    const conn = await fetch(`/api-delete-tweet`, {
        method: "DELETE",
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)

    tweet = document.querySelector("#tweet_id")
    console.log( tweet)
    tweet.remove();

    
    // function closeModalDeleteTweet() {
    //     document.querySelector("#modal_delete_tweet").classList.remove("hidden");
    // }
}
