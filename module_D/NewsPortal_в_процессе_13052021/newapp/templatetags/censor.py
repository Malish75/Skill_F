from django import template

# регистрируем наш фильтр
register = template.Library()
@register.filter(name='censor')

# post.title|multiply:"<цензура>"
def censor(value, arg):  # value|censor:arg
    bad_words = {
        'дурак',
        'дура',
        'сука',
        'жопа',
    }
    list_value = value.split(' ')
    for bad_word in bad_words:
        for i in range(len(list_value)):
            if bad_word in list_value[i].lower():
                list_value[i] = arg

    return ' '.join(list_value)