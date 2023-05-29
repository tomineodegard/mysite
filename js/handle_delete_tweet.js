async function handleDeleteTweet() {
    const frm = event.target
    const conn = await fetch(`/api-delete-tweet`, {
        method: "DELETE",
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)

    tweet = document.querySelector(`#tweet_id`)
    tweet.remove();
}
