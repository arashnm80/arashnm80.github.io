---
layout: page
title: C'est ma vie
---

<span id="sentence-container">I leave or live, <strong>this is my life.</strong></span><br>
**So what am I going to do with it, who do I choose to be and what do I choose to do [now](../no-time-for-caution)?**

<script>
document.addEventListener("DOMContentLoaded", function() {
    const sentences = [
        "I <a href=\"../c'est-la-vie\">leave or live</a>",
        "I accept or refuse",
        "I am or I'm not",
        "I do or do not",
        "I can or can't",
        "I act or don't act",
        "I try or don't try",
        "I have or don't have",
        "I like or don't like",
        "I need or don't need",
        "I rest or don't rest",
        "I want or don't want",
        "I fight or don't fight",
        "I choose or don't choose",
        "Best or worst",
        "Depression or euphoria",
        "Easy or hard",
        "Everything or nothing",
        "Fair or unfair",
        "Fast or slow",
        "Free or slaved",
        "Lion or rat",
        "Lonely or belonging",
        "Paradise or hell",
        "Pleasure or pain",
        "Predictable or chaotic",
        "Rich or poor",
        "Safe or risky",
        "Simple or complicated",
        "Strong or weak",
        "Sure or doubtful",
        "Victim or vigilante",
        "Win or lose",
    ];

    const boldText = "this is my life."; // The bold text you want to append

    const sentenceContainer = document.getElementById('sentence-container');

    function getRandomSentence() {
        const randomIndex = Math.floor(Math.random() * sentences.length);
        return sentences[randomIndex];
    }

    function showNextSentence() {
        sentenceContainer.style.opacity = 0; // Start fade-out effect

        setTimeout(() => {
            const randomSentence = getRandomSentence();
            sentenceContainer.innerHTML = randomSentence + ', <strong>' + boldText + '</strong>';
            sentenceContainer.style.opacity = 1; // Start fade-in effect
        }, 500); // Wait for fade-out to complete before changing the text
    }

    // // Set initial sentence
    showNextSentence()

    // Change sentence every few seconds
    setInterval(showNextSentence, 4000);

    // Set up initial fade-in effect
    sentenceContainer.style.transition = 'opacity 0.5s ease-in-out';
});
</script>

<!-- <style>
#sentence-container {
    transition: opacity 0.5s ease-in-out;
    opacity: 1;
    /* font-size: 1.5em;
    margin: 20px; */
}
</style> -->
