---
layout: default
title: Example Page
---

## Example Page

<div id="items">
- <span class="tag core">⬤ core</span> Item 1
- <span class="tag quality">⬤ quality level</span> Item 2
- <span class="tag core">⬤ core</span> Item 3
- <span class="tag quality">⬤ quality level</span> Item 4
</div>

<button onclick="filterItems('core')">Show Core Tags</button>
<button onclick="filterItems('quality')">Show Quality Level Tags</button>
<button onclick="filterItems('all')">Show All</button>

<script>
function filterItems(tag) {
    var items = document.getElementById('items').getElementsByTagName('span');
    for (var i = 0; i < items.length; i++) {
        var item = items[i];
        if (tag === 'all' || item.classList.contains(tag)) {
            item.parentElement.style.display = 'list-item'; // Show the item
        } else {
            item.parentElement.style.display = 'none'; // Hide the item
        }
    }
}
</script>
