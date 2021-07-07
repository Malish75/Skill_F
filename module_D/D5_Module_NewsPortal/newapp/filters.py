from django_filters import FilterSet
from .models import Post
from django.forms import DateInput
import django_filters


class PostFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title',
                                      lookup_expr='icontains',
                                      label='Заголовок')
    datetime = django_filters.DateFilter(field_name='time_in_new_post',
                                         widget=DateInput(attrs={'type': 'date'}),
                                         lookup_expr='gt', label='Не позднее')

    # Здесь в мета классе надо предоставить модель и указать поля по которым будет фильтроваться (т.е. подбираться) информация
    class Meta:
        model = Post
        fields = (
            'title',
            'datetime',
        )
        fields = {
            'author': ['exact'],
        }
