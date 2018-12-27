// Sticky navbar (sticks to the top even when you scroll down)
window.onscroll = function() { controlSticky()}; // keep on checking if the user has scrolled

var navbar = document.querySelector("nav"); // get the navbar element
var sticky = navbar.offsetTop; // get where the navbar is from the top

function controlSticky() {
	if (window.pageYOffset > sticky) { // if page is further down than the navbar's position
		navbar.classList.add("sticky"); // add the sticky class and let the css take over
	} else { // if at the top of page
		navbar.classList.remove("sticky"); // remove the temporary sticky class (restore default navbar)
	}
}

/** 
Known issue: When scrolling down and then back up, the navbar stays over some of the page's top elements, and the user can't scroll up further.
Perhaps fixed by changing comparison of pageYOffset and sticky from >= to >, AND setting navbar's z-index css property value to 1.
**/

// reference: https://www.w3schools.com/howto/howto_js_navbar_sticky.asp