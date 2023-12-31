from django import template

register = template.Library()


@register.filter(name='placeholder')
def placeholder(form_field, text):
    form_field.field.widget.attrs['placeholder'] = text
    return form_field
