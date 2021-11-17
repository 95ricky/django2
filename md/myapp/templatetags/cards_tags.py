from django import template

register = template.Library()

#template안에 있는 Library()라는 태그 생성 함수
@register.simple_tag(takes_context=True) 
def param_replace(context, **kwargs):
    d = context['request'].GET.copy() 
    for k, v in kwargs.items(): 
        d[k] = v

    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()