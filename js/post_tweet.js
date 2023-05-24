async function tweet() {
    const frm = event.target;
   
    const conn = await fetch("/api-tweet", {
     method: "POST",
     body: new FormData(frm),
    });
    const data = await conn.json();

    if (!conn.ok){
      console.log("Could nok tweet")
      return
  }


  // let tweetImageDataSaved;
  //   if (frm.tweet_image.files.length) {
  //       let formData = new FormData(frm);
  //       formData.append("tweet_id", dataata.tweet_id)

  //       const tweetImageConn = await fetch("/upload-tweet-image", {
  //           method: "POST",
  //           body: formData
  //       })
  //       const tweetImageData = await tweetImageConn.json()
  //       console.log(tweetImageData)
  //       tweetImageDataSaved = tweetImageData
  //   }

  //   if (!tweetImageDataSaved) {
  //       tweetImageDataSaved = "";
  //   } 

    

    let user_is_verified = data.cookie_user.user_is_verified
    if (data.cookie_user.user_is_verified == "0") {
      user_is_verified = "";
    }

    document.querySelector("#welcome_back").insertAdjacentHTML("afterend",

    `
    <div class="flex w-full border-t border-gray-600 overflow-hidden">
    <!-- left col -->
    <div class="p-4 flex flex-col justify-between items-center">
      <a href="${data.cookie_user.username}">
        <img src="/images/profilepictures/${data.cookie_user.user_profile_picture}" class="w-12 h-auto rounded-full object-cover">
      </a>
    </div>
     <!-- left col end -->
     <!-- right -->
     <div class="w-full pr-4 pt-4 pb-4">
      <div class="flex justify-between">
          <a href="${data.cookie_user.username}" class="flex justify-between gap-2 items-center text-base font-medium text-white">
          ${data.cookie_user.user_firstname} ${data.cookie_user.user_lastname}


          ${user_is_verified &&
            `<a href="/${data.cookie_user.user_username}" class="flex items-center">
                <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-label="Verified account" role="img" class="" data-icon-verified="icon-verified" width="20" height="20">
                    <g fill="#1D9BF0">
                        <path d="M22.25 12c0-1.43-.88-2.67-2.19-3.34.46-1.39.2-2.9-.81-3.91s-2.52-1.27-3.91-.81c-.66-1.31-1.91-2.19-3.34-2.19s-2.67.88-3.33 2.19c-1.4-.46-2.91-.2-3.92.81s-1.26 2.52-.8 3.91c-1.31.67-2.2 1.91-2.2 3.34s.89 2.67 2.2 3.34c-.46 1.39-.21 2.9.8 3.91s2.52 1.26 3.91.81c.67 1.31 1.91 2.19 3.34 2.19s2.68-.88 3.34-2.19c1.39.45 2.9.2 3.91-.81s1.27-2.52.81-3.91c1.31-.67 2.19-1.91 2.19-3.34zm-11.71 4.2L6.8 12.46l1.41-1.42 2.26 2.26 4.8-5.23 1.47 1.36-6.2 6.77z" fill="#1D9BF0"></path>
                    </g>
                </svg>
            </a>`
            }

            <p class="text-sm text-zinc-500 font-medium">
              <strong>@</strong>${data.cookie_user.username}
            </p>
          </a>


            <!-- ellipse icon -->
            <div>
              <svg width="32" height="22" viewBox="0 0 24 24" class="ml-auto text-twitterLightGray">
                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                  d="M6.75 12a.75.75 0 1 1-1.5 0a.75.75 0 0 1 1.5 0Zm6 0a.75.75 0 1 1-1.5 0a.75.75 0 0 1 1.5 0Zm6 0a.75.75 0 1 1-1.5 0a.75.75 0 0 1 1.5 0Z" />
              </svg>
            </div>
      </div>
       <!-- tweet userinfo end -->
       
       <!-- tweet content -->
       <div class="mt-4">
        ${data.tweet_message}
       </div>
      <!-- tweet content end -->

      <!-- icons for each tweet -->
      <!-- replies -->
       <div class="flex justify-between mt-4 text-twitterDarkGray pr-6 pb-2">
         <div class="flex gap-2 items-center text-twitterLightGray hover:text-twitterBlue">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
          </svg>                 
           <p class="">${data.tweet_total_replies}</p>
         </div>

        <!-- retweets -->
         <div class="flex gap-2 items-center text-twitterLightGray hover:text-twitterGreen">
           <svg width="24" height="24" viewBox="0 0 21 21" class=""><g fill="none" fill-rule="evenodd" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m13.5 13.5l3 3l3-3"/><path d="M9.5 4.5h3a4 4 0 0 1 4 4v8m-9-9l-3-3l-3 3"/><path d="M11.5 16.5h-3a4 4 0 0 1-4-4v-8"/></g></svg>
           <span class="">${data.tweet_total_retweets}</span>
         </div>

         <!-- likes -->
         <div class="flex gap-2 items-center text-twitterLightGray hover:text-twitterRed">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="w-6 h-6" stroke-width="1.5" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
          </svg>          
           <span class="">${data.tweet_total_likes}</span>
         </div>

         <!-- dislikes -->
         <!-- <div class="flex gap-2 items-center">
           <svg width="20" height="20" viewBox="0 0 20 20" class="w-6 h-6 text-twitterLightGray hover:text-twitterBlue"><path fill="currentColor" fill-opacity=".89" fill-rule="evenodd" d="M15.807.939c.396.367.655 1.133.706 1.595c.59.366 1.288 1.104 1.349 2.494c1.053.731 1.853 2.083.854 4.06c.58.54 1.227 2.188.395 3.516c-.969 1.552-3.075 1.66-5.174 1.383c.56 1.565.77 3.009-.116 4.488C12.94 19.787 11.724 20 11.308 20c-1.138 0-1.918-.979-2.234-2.283c-.115-.364-.246-1.224-.297-1.45c-.265-1.44-1.156-2.592-2.67-3.453a11.392 11.392 0 0 0-2.123-.946h-2.34c-.521 0-1.144-.527-1.144-1.165V3.067c.074-.722.475-1.082 1.202-1.082h3.11c1.364-.31 2.724-.642 4.079-.995C10.2.637 10.487.52 11.403.268c2.053-.532 3.478-.24 4.404.67Zm-2.382.424c-.819 0-1.856.252-2.316.399c-.162.051-.446.135-.745.221l-.3.087l-.288.082l-.56.158s-1.41.378-4.173 1.02c-.103.012-.158.02-.166.022v7.38c1.511.582 2.688 1.288 3.53 2.118c1.264 1.244 1.615 2.368 1.822 3.807c.118.723.309 1.306.597 1.705a.65.65 0 0 0 .342.251c.147.047.35.05.783-.184c.433-.236.99-.853 1.095-1.772c.07-.893-.17-1.667-.492-2.481a15.705 15.705 0 0 0-.357-.822c-.218-.413.11-1.099.786-.95c.906.255 3.154.6 4.422 0c.737-.427.92-1.116.547-2.066a1.74 1.74 0 0 0-.495-.553c-.17-.102-.502-.544-.103-1.045c.396-.635.975-1.928-.49-2.734a.656.656 0 0 1-.34-.57c-.02-.274.024-1.29-.73-1.744c-.18-.097-.397-.177-.52-.41c-.078-.154-.103-.528-.103-.528c-.103-.632-.245-1.222-1.746-1.391ZM3.519 3.348H1.861v7.157h1.658V3.348Z"/></svg>
           <span class="">{{tweet["tweet_total_dislikes"]}}</span>
         </div> -->

        <!-- views -->
         <svg width="24" height="24" viewBox="0 0 512 512" class="w-6 h-6 text-twitterLightGray hover:text-twitterBlue"><path fill="currentColor" d="M128 496H48V304h80Zm224 0h-80V208h80Zm112 0h-80V96h80Zm-224 0h-80V16h80Z"/></svg>
         
         <!-- share -->
         <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-twitterLightGray hover:text-twitterBlue">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
        </svg>
        
        </div>
       <!-- icons for each tweet end -->
     </div>
   </div> `
    )


    // empty the input field from the form
    frm[0].value = "";
};