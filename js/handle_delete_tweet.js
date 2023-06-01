async function handleDeleteTweet() {
    
    const frm = event.target
    const conn = await fetch(`/api-delete-tweet`, {
        method: "DELETE",
        body: new FormData(frm)
    })
    const data = await conn.json()
    // data.info ===  "tweet is deleted" ? closeModal() : location.href = `/`
    console.log(data)

    tweet = document.querySelector("#tweet_id")
    console.log( tweet)
    tweet.remove();

    function closeModal() {
        document.querySelector("#tweetOptionsModal").classList.remove("hidden");
    }
    
}
