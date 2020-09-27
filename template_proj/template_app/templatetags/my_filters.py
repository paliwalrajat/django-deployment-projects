from django import template

register = template.Library()

# THIS METHOD BELOW I USE "DECORATOR" AND AFTER THAT I USED SIMPLE METHOD THAT YOU SEE IN LAST LINE ( BOTH WORKS )
@register.filter(name='cut')
def cut(value,arg):
    return value.relpace(arg,'')

# I CAN USE THIS METHOD ALSO ->
# register.filter('cut',cut)
