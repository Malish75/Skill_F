from django_filters import FilterSet
from .models import Post
from django.forms import DateInput
​import django_filters
​

class PostFilter(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок')
    datetime = django_filters.DateFilter(field_name='datetime', widget=DateInput(attrs={'type': 'date'}),  lookup_expr='gt', label='Позже даты')
​
    class Meta:
        model = Post
        fields = {
            'author_id__user_id__username': ['icontains'],
        }