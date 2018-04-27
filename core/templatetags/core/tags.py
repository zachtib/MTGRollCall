import re

from django import template
from django.urls import reverse, NoReverseMatch
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def nav(context, url, text):
    try:
        url = reverse(url)
    except NoReverseMatch:
        pass

    # Special case for landing page
    pattern = f'^{url}$' if url == '/' else f'^{url}'

    path = context['request'].path
    active = re.search(pattern, path)
    return mark_safe(f'<li class="nav-item{" active" if active else ""}">'
                     f'<a class="nav-link" href="{url}">{text}</a>'
                     f'</li>')
