---
layout: page
title: C'est ma vie
---

<!-- 
I [leave or live](../c'est-la-vie), **this is my life.**  
I am or I'm not, **this is my life.**  
I do or do not, **this is my life.**  
I can or I can't, **this is my life.**  
I act or don't act, **this is my life.**  
I try or don't try, **this is my life.**  
I have or don't have, **this is my life.**  
I like or don't like, **this is my life.**  
I need or don't need, **this is my life.**  
I want or don't want, **this is my life.**  
I choose or don't choose, **this is my life.**  
I accept or refuse, **this is my life.**  
Win or lose, easy or hard, possible or impossible, **this is my life.**  
Best or worst, black or white, paradise or hell, **this is my life.**  
**So what am I going to do with it, who do I choose to be and what do I choose to do [now](../no-time-for-caution)?** -->


<span id="sentence-container">I leave or live, <strong>this is my life.</strong></span><br>
**So what am I going to do with it, who do I choose to be and what do I choose to do [now](../no-time-for-caution)?**

<script>
document.addEventListener("DOMContentLoaded", function() {
    const sentences = [
        "I leave or live",
        "I am or I'm not",
        "I do or do not",
        "I can or can't",
        "I act or don't act",
        "I try or don't try",
        "I have or don't have",
        "I like or don't like",
        "I need or don't need",
        "I want or don't want",
        "I fight or don't fight",
        "I choose or don't choose",
        "I accept or refuse",
        "Win or lose, easy or hard, possible or impossible",
        "Best or worst, black or white, paradise or hell",
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

    // Change sentence every 3 seconds
    setInterval(showNextSentence, 3000);

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