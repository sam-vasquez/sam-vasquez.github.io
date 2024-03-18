---
title: "Index of Notes"
permalink: /notes/
---

{% include base_path %}

{% for page in site.notes %}
    {% include note.html %}
{% endfor %}

