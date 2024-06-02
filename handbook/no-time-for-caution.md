---
layout: page
title: No time for caution
---

<!-- 
<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/5aaXqH8rgKZxg61HjECldi?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
-->

<div id="disappearing-text"></div>
<br>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Initial text
    let text = "Time is the most precious asset and ultimate currency of my life.";

    // Get the placeholder element
    const textElement = document.getElementById("disappearing-text");

    // Function to update text content
    function updateText() {
        if (text.length > 0) {
            textElement.textContent = text;
            text = text.slice(1);
            if (text[0] == " ") {
                text = text.slice(1);
            }
        } else {
            clearInterval(intervalId); // Stop the interval when text is empty
        }
    }

    // Call the function immediately to display the initial text
    updateText();

    // Set an interval to update text every second (1000 milliseconds)
    const intervalId = setInterval(updateText, 1000);
});
</script>
