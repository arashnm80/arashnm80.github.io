<div id="disappearing-text"></div>
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
</script>