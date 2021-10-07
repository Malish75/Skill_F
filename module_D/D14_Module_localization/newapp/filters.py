from django_filters import FilterSet
from .models import Post
from django.forms import DateInput
import django_filters
from django.utils.translation import gettext as _

class PostFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title',
                                      lookup_expr='icontains',
                                      label=_('По заголовку'))

    content_new_post = django_filters.CharFilter(field_name='content_new_post',
                                      lookup_expr='icontains',
                                      label=_('По тексту'),
                                                 )

    datetime = django_filters.DateFilter(field_name='time_in_new_post',
                                         widget=DateInput(attrs={'type': 'date'}),
                                         lookup_expr='gt', label=_('Не позднее'),
                                         )

    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация
    class Meta:
        model = Post
        fields = (
            'title',
            'content_new_post'
            'datetime',
        )
        fields = {
            'author': ['exact'],
        }
