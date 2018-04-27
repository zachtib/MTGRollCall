import re

from django import template
from django.urls import reverse, NoReverseMatch
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def nav_element(context, url, text):
    try:
        reversed = reverse(url)
        if reversed == '/':
            # Special case for landing page
            pattern = '^%s$' % reversed
        else:
            pattern = '^%s' % reversed
    except NoReverseMatch:
        pattern = url

    path = context['request'].path
    active = True if re.search(pattern, path) else False
    return mark_safe(f'''<li class="nav-item{" active" if active else ""}">
                   <a class="nav-link" href="{reverse(url)}">{text}</a>
               </li>''')
