async function tweet() {
  const frm = event.target;
  const conn = await fetch("/api-tweet", {
   method: "POST",
   body: new FormData(frm),
  });

  const data = await conn.json();
  console.log(data);

  let uploadedImg; 
 
  if (frm.tweet_image.files.length) {
   console.log("Image is uploaded succesfully");
   let formData = new FormData(frm);
   formData.append("tweet_id", data.tweet_id);

   console.log(formData)
 
   const connection = await fetch(`/api-upload-tweet-image`, {
    method: "POST",
    body: formData,
   });

   const dataTweetImg = await connection.json();
   console.log(dataTweetImg);
 
   uploadedImg = dataTweetImg.tweet_image;
  }
 
  if (!uploadedImg) {
   uploadedImg = "";
  }

   // ----- check if the user i verified or not, this is for the insertAdjecentHTML
  let user_is_verified = data.cookie_user.user_is_verified
  if (data.cookie_user.user_is_verified == 0) {
    user_is_verified = "";
  }

  let user_profile_picture = data.cookie_user.user_profile_picture
  if (data.cookie_user.user_profile_picture == "") {
    user_profile_picture = `<img src="images/profilepictures/default_avatar.png" class="w-12 h-auto rounded-full object-cover">`;
  }


  
  // ----- insertAdjecentHTML with new tweet created
  document.querySelector("#welcome_back").insertAdjacentHTML(
   "afterend",
   `
   <div id="tweet_id" class="flex w-full border-t border-gray-600 overflow-hidden">
    <!-- left col -->
    <div class="p-4 flex flex-col justify-between items-center">
    ${user_profile_picture &&
      `<a href="/${data.cookie_user.username}">
        <img src="images/profilepictures/${data.cookie_user.user_profile_picture}" class="w-12 h-auto rounded-full object-cover">
      </a>`
      }
    </div>
     <!-- left col end -->
     <!-- right -->
     <div class="w-full pr-4 pt-4 pb-4">
      <div class="flex justify-between">
        <div class="flex gap-4">
          <a href="/${data.cookie_user.username}" class="flex justify-between gap-2 items-center text-base font-medium text-white">
            ${data.cookie_user.user_firstname} ${data.cookie_user.user_lastname}

            ${user_is_verified &&
            `<a href="/${data.cookie_user.username}" class="flex items-center">
              <svg width="20" height="20" viewBox="0 0 24 24" class="text-twitterBlue">
                  <path fill="currentColor" d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"/>
              </svg>
            </a>`
            }

            <p class="text-sm text-zinc-500 font-medium transition ease-in-out duration-150">
              @${data.cookie_user.username}
            </p>
          </a>
          <!-- timestamp -->
          <div class="text-sm text-zinc-500 font-medium items-center">
            <p class="epochDayMonth">Just now</p>
          </div>
        </div>

          <!-- ellipse icon --> 
            <button onclick="displayModalDeleteTweet()" type="button">
              <svg width="32" height="22" viewBox="0 0 24 24" class="ml-auto text-twitterLightGray hover:text-twitterBlue">
                <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                  d="M6.75 12a.75.75 0 1 1-1.5 0a.75.75 0 0 1 1.5 0Zm6 0a.75.75 0 1 1-1.5 0a.75.75 0 0 1 1.5 0Zm6 0a.75.75 0 1 1-1.5 0a.75.75 0 0 1 1.5 0Z" />
              </svg>
            </button>
       </div>
       <!-- tweet userinfo end -->
       
       <!-- tweet content -->
       <div class="mt-4">
       ${data.tweet_message}

       ${
        uploadedImg &&
        `
        <img src="images/tweet_images/${uploadedImg}" class="w-full mt-4 max-h-96 rounded-lg object-contain">
       `
       }
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

        <!-- views -->
         <svg width="24" height="24" viewBox="0 0 512 512" class="w-6 h-6 text-twitterLightGray hover:text-twitterBlue"><path fill="currentColor" d="M128 496H48V304h80Zm224 0h-80V208h80Zm112 0h-80V96h80Zm-224 0h-80V16h80Z"/></svg>
         
         <!-- share -->
         <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-twitterLightGray hover:text-twitterBlue">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
        </svg>
        
        </div>
       <!-- icons for each tweet end -->
     </div>
   </div>

   <!-- Full screen overlay element -->
<div class="hidden fixed z-40 w-screen h-screen inset-0 bg-gray-700 bg-opacity-75" id="modal_delete_tweet">
    <!-- Dialog start -->
    <div class="fixed z-50 w-screen h-screen sm:top-[30%] sm:left-1/2 sm:-translate-x-1/2 sm:-translate-y-1/4 bg-black sm:rounded-xl space-y-5 drop-shadow-lg sm:w-[600px] sm:h-auto">
        <!-- Form start -->
        <form onsubmit="handleDeleteTweet(); return false">
            <div class="bg-black rounded-lg w-full h-fit flex flex-col justify-center items-center mx-auto my-0 md:h-fit md:my-4">
                <!-- Modal navigation -->
                <div class="p-4 flex items-center justify-between">
                    <div class="flex gap-2">
                        <button onclick="closeModalDeleteTweet()" type="button">
                            <svg class="modal" height="22" viewbox="0 0 15 15" width="22" xmlns="http://www.w3.org/2000/svg">
                            <path clip-rule="evenodd" d="M11.782 4.032a.575.575 0 1 0-.813-.814L7.5 6.687L4.032 3.218a.575.575 0 0 0-.814.814L6.687 7.5l-3.469 3.468a.575.575 0 0 0 .814.814L7.5 8.313l3.469 3.469a.575.575 0 0 0 .813-.814L8.313 7.5l3.469-3.468Z" fill="currentColor" fill-rule="evenodd"></path>
                            </svg>
                        </button>
                        <p class="text-base text-white">Are you sure you want to delete this tweet?</p>
                    </div>
                </div>
                <!-- Modal navigation end -->
                    <input type="text" name="tweet_id" id="${data.tweet_id}" value="${data.tweet_id}" style="display: none">
                    <button onclick="closeModalDeleteTweet()" type="submit" class="cursor-pointer bg-twitterRed py-2 w-1/2 rounded-full text-white flex justify-center">Delete</button>
                </div>
        </form>
        <!-- Form end -->
    </div>
</div>
<!-- Dialog end -->
<!-- Full screen overlay element end -->
    `
  );

  const tweetPreviewContainer = document.querySelectorAll(".tweetPreviewContainer");
  // add hidden to tweetPreviewContainer and reset form when tweet is submitted
  tweetPreviewContainer[0].classList.add("hidden");
  frm.reset();
 }
  
  
  function previewTweetImg() {
    const tweetPreviewContainer = document.querySelectorAll(".tweetPreviewContainer");
    const tweetImgPreview = document.querySelectorAll(".tweetImgPreview");
    const [tweetImage] = tweetImgUpload.files;
  
    if(tweetImage) {
      tweetImgPreview[0].src = URL.createObjectURL(tweetImage);
      tweetPreviewContainer[0].classList.remove("hidden");
      console.log("remove hidden from tweetPreviewContainer", tweetPreviewContainer[0])
    } else {
      tweetPreviewContainer[0].classList.add("hidden");
    }

  
  // when the user clicks the X, the preview is cleared
   document.querySelectorAll(".closePreview")[0].addEventListener("click", () => {
    console.log("add hidden to tweetPreviewContainer")
    tweetPreviewContainer[0].classList.add("hidden");
    tweetImgPreview[0].src = URL.revokeObjectURL(tweetImage);
    document.querySelector('#tweetImgUpload').value = "";
    return
   });
   
  }