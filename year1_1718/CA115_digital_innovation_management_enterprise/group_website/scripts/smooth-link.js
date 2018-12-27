smoothElements = document.querySelectorAll(".smooth-link")

smoothElements.forEach(smoothElem => {
    smoothElem.addEventListener("click", function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// reference: https://stackoverflow.com/questions/7717527/smooth-scrolling-when-clicking-an-anchor-link