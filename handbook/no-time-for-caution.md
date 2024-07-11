---
layout: page
title: No time for caution
---

> **Time is the most precious and ultimate currency of my life.**

<!-- Too many days, months and years of my life have passed and too few are left. I have to start acting right now and think about parameters and improvements over time later.


> Time's running out like a cup of coffee, so whatever I have to do it right fu*king now.

> It's always late to start, tomorrow much later than today.

> This life, this year, this year, this second
![this-life-this-day-this-day-this-second](../../assets/this-life-this-day-this-day-this-second.jpg)

> I won't get rich by renting out my time.

### Time Travel
> Assess every choice with a single question: "If I time-travel to past, do I repeat it again the same?"

> Do I live my life in such a way that I would be willing to repeat it again and again, forever?

> Would I have chosen to be born or not?

> I just try to live every day as if I've deliberately come back to this one day, to enjoy it, as if it was the full final day of my extraordinary, ordinary life.

### Make every second count
Either I sleep, work, sex, watch movie, exercise, play, fight, ... I should use every second for sth worthwhile. -->







<!-- <div id="disappearing-text"></div>
<br>

<script>
document.addEventListener("DOMContentLoaded", function() {
    // Initial text
    let text = "Time is the most precious, higest priority and ultimate currency of my life.";
    // let text = 'Time is the most <a href="../fight">now</a> precious asset and ultimate currency of my life.';

    // Get the placeholder element
    const textElement = document.getElementById("disappearing-text");

    // find the nth occurrence of a character
    function findNthOccurrence(str, char, n) {
        let count = 0;
        for (let i = 0; i < str.length; i++) {
            if (str[i] === char) {
                count++;
                if (count === n) {
                    return i; // Return the index of the nth occurrence
                }
            }
        }
        return -1; // Return -1 if the nth occurrence is not found
    }

    // Function to update text content
    function updateText() {
        if (text.length > 0) {
            textElement.textContent = text;
            // textElement.innerHtml = "<p>" + text + "</p>";
            if (text[0] != "<"){
                text = text.slice(1);
                if (text[0] == " ") {
                    text = text.slice(1);
                }
            }
            // } else {
            //     var startIndex = findNthOccurrence(text, ">", 1)
            //     var endIndex = findNthOccurrence(text, "<", 2)

            //     var oldElement = text.substring(startIndex + 1, endIndex)
            //     if (oldElement.length == 1) {
            //         var endIndexOfElement = findNthOccurrence(text, ">", 2)
            //         text = text.substring(endIndexOfElement + 1)
            //     } else {

            //         text = text.replace("/"+ oldElement.slice(1) + "/", "cat");
            //     }
            // }
        } else {
            clearInterval(intervalId); // Stop the interval when text is empty
        }
    }

    // Call the function immediately to display the initial text
    updateText();

    // Set an interval to update text every second (1000 milliseconds)
    const intervalId = setInterval(updateText, 1000);
});
</script> -->