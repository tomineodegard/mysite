document.querySelector("#welcome_back").insertAdjacentHTML(
    "afterend",
    `
    <div class="flex w-full cursor-pointer pb-4 overflow-hidden">
   <!-- left -->
   <div class="p-4 flex flex-col justify-between">
    <img src="images/user_profile_picture/${data.cookie_user.user_profile_picture}" class="w-16 rounded-full" alt="" />
   </div>
   <!-- right -->
   <div class="w-full pr-4 pt-4">
    <!-- username -->
    <div class="flex flex-col">
     <p class="flex items-center text-base leading-6 font-medium text-white">
      <a href="/${data.cookie_user.username} ">
       <span class="text-inherit hover:underline"> ${data.cookie_user.user_firstname} ${data.cookie_user.user_lastname}</span>
      </a>
      <!-- ignore prettier -->
      ${user_is_verified &&
       `<a href="/${data.cookie_user.username}" class="flex items-center">
         <svg aria-label="Verified account" width="20" height="20" viewBox="0 0 24 24" class="text-twitterBlue">
           <path fill="currentColor" d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"/>
         </svg>
       </a>`
       }
    
      <span class="ml-1 text-sm leading-5 font-medium text-trending group-hover:text-gray-300 transition ease-in-out duration-150"> @${data.cookie_user.username}</span>
      <span class="mx-1 inline-block bg-trending h-1 w-1 mb-[2.5px] rounded-full"></span><span class="tweet_timestamp text-sm leading-5 font-medium text-trending">Just now</span>
      <!-- ... icon -->
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 ml-auto text-zinc-400 hover:text-sky-600 hover:cursor-pointer">
       <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z"></path>
      </svg>
     </p>
     <div class="flex flex-col text-base text-white">
      <p>${data.tweet_message}</p>
      
      ${
       uploadedImg &&
       `
      <img src="images/tweet_images/${uploadedImg}" class="rounded-xl mt-4" />
      `
      }
      
     </div>
    </div>
    <!-- icons -->
    <div class="flex justify-between mt-4 text-gray-700 pr-6 pb-2">
     <!-- comment -->
     <div class="flex items-center cursor-pointer group">
      <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
       <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" class="fill-gray-500 group-hover:fill-[#1D9BF0] transition ease-in-out" width="20" height="20">
        <g>
         <path d="M1.751 10c0-4.42 3.584-8 8.005-8h4.366c4.49 0 8.129 3.64 8.129 8.13 0 2.96-1.607 5.68-4.196 7.11l-8.054 4.46v-3.69h-.067c-4.49.1-8.183-3.51-8.183-8.01zm8.005-6c-3.317 0-6.005 2.69-6.005 6 0 3.37 2.77 6.08 6.138 6.01l.351-.01h1.761v2.3l5.087-2.81c1.951-1.08 3.163-3.13 3.163-5.36 0-3.39-2.744-6.13-6.129-6.13H9.756z"></path>
        </g>
       </svg>
      </span>
      <span class="text-sm text-gray-500 group-hover:text-[#1D9BF0] transition ease-in-out">
      ${data.tweet_total_replies}</span>
     </div>
     <!-- retweet -->
     <div class="flex items-center cursor-pointer group">
      <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
       <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" class="fill-gray-500 group-hover:fill-emerald-500 transition ease-in-out" width="20" height="20">
        <g>
         <path d="M4.75 3.79l4.603 4.3-1.706 1.82L6 8.38v7.37c0 .97.784 1.75 1.75 1.75H13V20H7.75c-2.347 0-4.25-1.9-4.25-4.25V8.38L1.853 9.91.147 8.09l4.603-4.3zm11.5 2.71H11V4h5.25c2.347 0 4.25 1.9 4.25 4.25v7.37l1.647-1.53 1.706 1.82-4.603 4.3-4.603-4.3 1.706-1.82L18 15.62V8.25c0-.97-.784-1.75-1.75-1.75z"></path>
        </g>
       </svg>
      </span>
      <span class="text-sm text-gray-500 group-hover:text-emerald-500 transition ease-in-out">${data.tweet_total_retweets}</span>
     </div>
     <!-- like -->
     <div class="flex items-center hover cursor-pointer group">
      <span class="group-hover:bg-pink-600/[0.15] transition ease-in-out rounded-full p-2">
       <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" class="fill-gray-500 group-hover:fill-pink-600 transition ease-in-out r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi" width="20" height="20">
        <g>
         <path
          d="M16.697 5.5c-1.222-.06-2.679.51-3.89 2.16l-.805 1.09-.806-1.09C9.984 6.01 8.526 5.44 7.304 5.5c-1.243.07-2.349.78-2.91 1.91-.552 1.12-.633 2.78.479 4.82 1.074 1.97 3.257 4.27 7.129 6.61 3.87-2.34 6.052-4.64 7.126-6.61 1.111-2.04 1.03-3.7.477-4.82-.561-1.13-1.666-1.84-2.908-1.91zm4.187 7.69c-1.351 2.48-4.001 5.12-8.379 7.67l-.503.3-.504-.3c-4.379-2.55-7.029-5.19-8.382-7.67-1.36-2.5-1.41-4.86-.514-6.67.887-1.79 2.647-2.91 4.601-3.01 1.651-.09 3.368.56 4.798 2.01 1.429-1.45 3.146-2.1 4.796-2.01 1.954.1 3.714 1.22 4.601 3.01.896 1.81.846 4.17-.514 6.67z"
         ></path>
        </g>
       </svg>
      </span>
      <span class="text-sm text-gray-500 group-hover:text-pink-600 transition ease-in-out">${data.tweet_total_likes}</span>
     </div>
     <!-- views -->
     <div class="hidden lg:flex items-center cursor-pointer group">
      <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
       <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" strok="" aria-hidden="true" class="fill-gray-500 group-hover:fill-[#1D9BF0] transition ease-in-out r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi" width="20" height="20">
        <g>
         <path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.004-10h2L6 21H4zm9.248 0v-7h2v7h-2z"></path>
        </g>
       </svg>
      </span>
      <span class="pl-2 text-sm text-gray-500 group-hover:text-[#1D9BF0] transition ease-in-out">${data.tweet_total_views}</span>
     </div>
     <!-- share -->
     <div class="flex items-center cursor-pointer group">
      <span class="group-hover:bg-[#1D9BF0]/[0.15] transition ease-in-out rounded-full p-2">
       <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true" class="fill-gray-500 group-hover:fill-[#1D9BF0] transition ease-in-out r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi" width="20" height="20">
        <g>
         <path d="M12 2.59l5.7 5.7-1.41 1.42L13 6.41V16h-2V6.41l-3.3 3.3-1.41-1.42L12 2.59zM21 15l-.02 3.51c0 1.38-1.12 2.49-2.5 2.49H5.5C4.11 21 3 19.88 3 18.5V15h2v3.5c0 .28.22.5.5.5h12.98c.28 0 .5-.22.5-.5L19 15h2z"></path>
        </g>
       </svg>
      </span>
     </div>
    </div>
   </div>
  </div>
     `
   );