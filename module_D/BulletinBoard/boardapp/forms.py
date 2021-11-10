from .models import Posts, Messages
from  django.forms import ModelForm, TextInput, Select, Textarea
import datetime

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title_post', 'text_post', 'category_post', ]
        widgets = {
            'title_post': TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Заголовок'
                }),
            'text_post': Textarea(attrs={
                "class": "form-control",
                'placeholder': 'Текст объявления'
                }),
            'category_post': Select(attrs={
                "class": "form-control",
                }),
            }


class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['text_message',]
        widgets = {
                'text_message': Textarea(attrs={
                "class": "form-control",
                'placeholder': 'Текст отклика'
                }),
        }