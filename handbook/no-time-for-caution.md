---
layout: page
title: No time for caution
---

<div id="disappearing-text"></div>
<!-- <h3 id="tick-tock"></h3> -->
<br>

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/5aaXqH8rgKZxg61HjECldi?utm_source=generator&theme=0" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Initial text
    let text = "Time is my most precious asset and it's running out like a cup of coffee. Whatever I'm gonna do I have to do it right now, cause how much time is left for me after all!?";

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

<!-- <script>
document.addEventListener("DOMContentLoaded", function() {
    // Get the placeholder element
    const tickTockElement = document.getElementById("tick-tock");

    // Initialize the state
    let isTick = true;

    // Function to switch text
    function switchText() {
        tickTockElement.textContent = isTick ? "tick" : "tock";
        isTick = !isTick;
    }

    // Call the function immediately to switch text
    switchText();

    // Set an interval to switch text every second (1000 milliseconds)
    setInterval(switchText, 1000);
});
</script> -->