async function tweet() {
    const frm = event.target;
   
    const conn = await fetch("/api-tweet", {
     method: "POST",
     body: new FormData(frm),
    });
    const data = await conn.json();


    console.log(data);

    document.querySelector("#welcome_back").insertAdjacentHTML(
        "afterend",

        `<div class="flex w-full border-t border-gray-600 overflow-hidden">
        <!-- left col -->
        <div class="p-4 flex flex-col justify-between">
          <a href="#">
            <img src="${data.cookie_user.user_profile_picture}" class="w-12 h-12 rounded-full object-cover">
          </a>
        </div>
         <!-- left col end -->
         <!-- right -->
         <div class="w-full pr-4 pt-4 pb-4">
          <!-- username -->
          <div class="flex justify-between">
              <a href="#" class="flex justify-between gap-2 items-center text-base font-medium text-white">
                ${data.cookie_user.user_firstname} ${data.cookie_user.user_lastname}
                <svg width="20" height="20" viewBox="0 0 24 24" class="text-sky-500"><path fill="currentColor" d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"/></svg>
                <p class="ml-1 text-sm text-gray-500 font-medium group-hover:text-gray-300 transition ease-in-out duration-150">
                ${data.cookie_user.username}
                </p>
              </a>
    
    
                <!-- ... icon -->
                <div>
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots w-6 h-6 ml-auto text-zinc-400 hover:text-sky-600 hover:cursor-pointer" viewBox="0 0 16 16">
                  <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
                </svg>
                </div>
          </div>
           <!-- tweet userinfo end -->
           
           <!-- tweet content -->
           <div class="mt-4">
             ${data.tweet_message}
             <a href="#">
               <img src="" class="w-full mt-4 max-h-96 rounded-lg object-contain">
             </a>
           </div>
          <!-- tweet content end -->
    
          <!-- icons for each tweet -->
          <!-- replies -->
           <div class="flex justify-between mt-4 text-gray-700 pr-6 pb-2">
             <div class="flex gap-2 items-center text-gray-400 hover:text-sky-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
              </svg>                 
               <p class="">0</p>
             </div>
    
            <!-- retweets -->
             <div class="flex gap-2 items-center text-gray-400 hover:text-green-500">
               <svg width="24" height="24" viewBox="0 0 21 21" class=""><g fill="none" fill-rule="evenodd" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m13.5 13.5l3 3l3-3"/><path d="M9.5 4.5h3a4 4 0 0 1 4 4v8m-9-9l-3-3l-3 3"/><path d="M11.5 16.5h-3a4 4 0 0 1-4-4v-8"/></g></svg>
               <span class="">0</span>
             </div>
    
             <!-- likes -->
             <div class="flex gap-2 items-center text-gray-400 hover:text-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" class="w-6 h-6" stroke-width="1.5" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
              </svg>          
               <span class="">0</span>
             </div>
    
            <!-- views -->
             <svg width="24" height="24" viewBox="0 0 512 512" class="w-6 h-6 text-gray-400 hover:text-sky-500"><path fill="currentColor" d="M128 496H48V304h80Zm224 0h-80V208h80Zm112 0h-80V96h80Zm-224 0h-80V16h80Z"/></svg>
             
             <!-- share -->
             <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-gray-400 hover:text-sky-500">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
            </svg>
            
            </div>
           <!-- icons for each tweet end -->
         </div>
       </div>`
    )
};
