// Title 'fades in'(goes from light to dark colour) slowly, animative effect

// classic 

var title = document.querySelector(".faded-out");
title.classList.add("fade-in");
//title.classList.remove("fade-in")
//title.classList.remove("faded-out")

/** to-do: 
-find a way to remove the 'fade-in' and 'faded-out' classes to restore the 'normal' class of the title.
Attempted Triedto use setTimeout() before removing the classes, so that the animation has some time to play out, but that broke things
-only show this for first time users
**/

// reference: https://www.abeautifulsite.net/a-clean-fade-in-effect-for-webpages