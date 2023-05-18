// from Hogwarts

"use strict"

let originalName = object.fullname.trim();

// ----- Cleaning first name
if (originalName.includes(" ")) {
    user.firstName = originalName.substring(originalName.indexOf(0), originalName.indexOf(" "));
  } else {
    user.firstName = originalName.substring(originalName.indexOf(0));
  }
  user.firstName = user.firstName.substring(0, 1).toUpperCase() + user.firstName.substring(1).toLowerCase();


// ----- Cleaning last name
if (originalName.includes(" ")) {
    user.firstName = originalName.substring(originalName.indexOf(0), originalName.indexOf(" "));
  } else {
    user.firstName = originalName.substring(originalName.indexOf(0));
  }
  user.firstName = user.firstName.substring(0, 1).toUpperCase() + user.firstName.substring(1).toLowerCase();
