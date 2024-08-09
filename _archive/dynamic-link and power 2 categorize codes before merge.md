
// JavaScript to dynamically set the text content based on href attribute
document.querySelectorAll('.dynamic-link').forEach(link => {
    const href = link.getAttribute('href').replace('./', '');
    link.textContent = href;
});


// categorize in power of 2 notion
document.addEventListener('DOMContentLoaded', function () {
// Get all the list items
const allItems = document.querySelectorAll('#all-items ul li');
const organizedItemsContainer = document.getElementById('organized-items');

// Initialize the starting variables
let section = 0;
let itemIndex = 0;

// Loop through the list items and categorize them by sections
while (itemIndex < allItems.length) {
    // Calculate the number of items for the current section (2^section)
    const itemsInSection = Math.pow(2, section);
    
    // Create a new section heading and div
    const sectionTitle = document.createElement('h3');
    sectionTitle.textContent = section;
    
    const sectionDiv = document.createElement('div');
    sectionDiv.classList.add('items');
    
    const sectionList = document.createElement('ol');
    
    // Add the items to the current section
    for (let i = 0; i < itemsInSection && itemIndex < allItems.length; i++) {
        sectionList.appendChild(allItems[itemIndex]);
        itemIndex++;
    }
    
    // Append the section to the organized-items container
    sectionDiv.appendChild(sectionList);
    organizedItemsContainer.appendChild(sectionTitle);
    organizedItemsContainer.appendChild(sectionDiv);
    
    // Move to the next section
    section++;
}
});