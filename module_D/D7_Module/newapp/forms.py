from django.forms import ModelForm, BooleanField
from .models import Post, Comment
from django import forms


# Создаём модельную форму
class PostForm(ModelForm):
    #check_box = BooleanField(label='Все проверил')  # добавляем галочку, или же true-false поле
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['title',
                  'content_new_post',
                  'category',
                  'author',
                  ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content_comments',
            # 'text',
        ]


class ContactForm(forms.Form):
    subject = forms.CharField(label="Тема", widget=forms.TextInput(attrs={"class":"form-control"}))   # тема письма
    content = forms.CharField(label="Текст", widget=forms.Textarea(attrs={"class":"form-control", "rows":5}))






'''создание форм - пример'''
# from django.forms import Form, CharField, IntegerField, EmailField
# class DummyForm(Form):
#     field1 = CharField()
#     field2 = IntegerField()
#     field3 = EmailField()