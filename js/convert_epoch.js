"use strict"


const userCreatedAt = document.querySelectorAll(".epoch");
userCreatedAt.forEach((e) => {
  const epochTimestamp = e.textContent;
  const date = new Date(epochTimestamp * 1000);
  const dateOptions = {
    year: 'numeric',
    month: "long",
  };
  const created_at = new Intl.DateTimeFormat("en-US", dateOptions).format(date);
  e.textContent = `${created_at}`;
});


const tweetCreatedAt = document.querySelectorAll(".epochDayMonth");
tweetCreatedAt.forEach((e) => {
  const epochTimestamp = e.textContent;
  const date = new Date(epochTimestamp * 1000);
  const dateOptions = {
    day: "numeric",
    month: "short",

  };
  const created_at = new Intl.DateTimeFormat("en-US", dateOptions).format(date);
  e.textContent = `${created_at}`;
});