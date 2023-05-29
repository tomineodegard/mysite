async function handleDeleteTweet() {
    const frm = event.target
    const conn = await fetch(`/api-delete-tweet`, {
        method: "DELETE",
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)
    tweet_id = document.querySelector(`#tweet_id`)
    console.log(tweet_id)
}
