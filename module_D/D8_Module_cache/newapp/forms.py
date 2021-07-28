from django.forms import ModelForm, Form
from .models import Post, Comment, Category
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
                  'is_published',
                  ]

# ''' а тут из ютуба'''
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=150)
#     content_new_post = forms.CharField()
#     is_published = forms.BooleanField()
#     category = forms.ModelChoiceField(queryset=Category.objects.all())
#     category = forms.MultipleChoiceField(choices=Category.objects.all().values('category_name'))



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