---
layout: default
title: Example Page
---

## Example Page

<div id="items">
- Item 1 <span class="tag core">⬤ core</span>
- Item 2 <span class="tag quality">⬤ quality level</span>
- Item 3 <span class="tag core">⬤ core</span>
- Item 4 <span class="tag quality">⬤ quality level</span>
</div>

<script>
function filterItems(tag) {
    var items = document.getElementById('items').getElementsByTagName('span');
    for (var i = 0; i < items.length; i++) {
        var item = items[i];
        if (tag === 'all' || item.classList.contains(tag)) {
            item.style.display = 'inline-block'; // Show the item
        } else {
            item.style.display = 'none'; // Hide the item
        }
    }
}
</script>

<button onclick="filterItems('core')">Show Core Tags</button>
<button onclick="filterItems('quality')">Show Quality Level Tags</button>
<button onclick="filterItems('all')">Show All</button>
