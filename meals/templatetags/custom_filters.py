from django import template

register = template.Library()

@register.filter(name='text_to_html')
def text_to_html(value):
    lines = value.split('\n')
    lines = ['<li>' + line.strip('· ').strip() + '</li>' if line.strip().startswith('·') else line for line in lines]
    return '<p>' + ''.join(lines) + '</p>'