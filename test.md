---
layout: default
title: Example Page
---

## Example Page

{% assign filter = page.filter | default: 'all' %}

- Item 1 {% if filter == 'core' %}<span class="tag core">⬤ core</span>{% endif %}
- Item 2 {% if filter == 'quality' %}<span class="tag quality">⬤ quality level</span>{% endif %}
- Item 3 {% if filter == 'core' %}<span class="tag core">⬤ core</span>{% endif %}
- Item 4 {% if filter == 'quality' %}<span class="tag quality">⬤ quality level</span>{% endif %}

[Show Core Tags](?filter=core)
[Show Quality Level Tags](?filter=quality)
[Show All](?filter=all)
