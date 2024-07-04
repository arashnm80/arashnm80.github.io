---
layout: page
title: C'est ma vie
---

<span id="sentence-container">I leave or live, <strong>this is my life.</strong></span><br>
**So what am I going to do with it, who do I choose to be and what do I choose to do [now](../no-time-for-caution)?**

<script>
document.addEventListener("DOMContentLoaded", function() {
    const sentences = [
        "<a href=\"../c'est-la-vie\">I leave or live</a>",
        "I accept or refuse",
        "I am or I'm not",
        "I do or don't",
        "I can or can't",
        "I act or don't act",
        "I try or don't try",
        "I feel or don't feel",
        "I have or don't have",
        "I like or don't like",
        "I need or don't need",
        "I rest or don't rest",
        "I want or don't want",
        "<a href='../fight'>I fight or don't fight</a>",
        "I choose or don't choose",
        "Best or worst",
        "Calm or stressed",
        "Certain or doubtful",
        "Euphoric or depressed",
        "Easy or hard",
        "<a href='../biggest-problem'>Everything or nothing</a>",
        "Fair or unfair",
        "Fast or slow",
        "Free or slave",
        "Lion or rat",
        "Lonely or belonging",
        "Male or female",
        "Moral or immoral",
        "Optional or compulsory",
        "Paradise or hell",
        "Pleasure or pain",
        "<a href='../uncertainty'>Predictable or chaotic</a>",
        "Proud or ashamed",
        "Red pill or blue",
        "Rich or poor",
        "Safe or risky",
        "Simple or complicated",
        "Strong or weak",
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
