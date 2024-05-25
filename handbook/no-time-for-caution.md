---
layout: page
title: No time for caution
---

<div id="disappearing-text"></div>
<!-- <h3 id="tick-tock"></h3> -->

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Initial text
    let text = "Time is my most precious asset and it's running out like a cup of coffee. Whatever I'm gonna do, I have to do it right now.";

    // Get the placeholder element
    const textElement = document.getElementById("disappearing-text");

    // Function to update text content
    function updateText() {
        if (text.length > 0) {
            textElement.textContent = text;
            text = text.slice(1);
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