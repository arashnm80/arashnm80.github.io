---
layout: page
title: Handbook
permalink: /handbook/
---

**This can be paradise, this can be hell. This is life, but whatever this is, this is my life. So what am I going to do with it, who do I choose to be and what do I choose to do now?**

### 0
<div class="items">
<ol>
<li><a href="./c'est-ma-vie">C'est ma vie</a> <button style="color:Black" onclick="filterItems('core')" class="tag core">⬤ core</button></li>
</ol>
</div>

### 1
<div class="items">
<ol>
<li><a href="./c'est-la-vie">C'est la vie</a> <button style="color:Black" onclick="filterItems('core')" class="tag core">⬤ core</button></li>
<li><a href="./no-time-for-caution">No time for caution</a> <button style="color:Black" onclick="filterItems('core')" class="tag core">⬤ core</button></li>
</ol>
</div>



<button onclick="filterItems('core')">⬤ core</button>
<button onclick="filterItems('quality')">⬤ quality level</button>
<button onclick="filterItems('all')">Show All</button>

<script>
function filterItems(tag) {
    var containers = document.getElementsByClassName('items');
    for (var j = 0; j < containers.length; j++) {
        var items = containers[j].getElementsByTagName('li');
        for (var i = 0; i < items.length; i++) {
            var item = items[i];
            if (tag === 'all' || item.querySelector('.tag').classList.contains(tag)) {
                item.style.display = 'list-item'; // Show the item
            } else {
                item.style.display = 'none'; // Hide the item
            }
        }
    }
}
</script>
