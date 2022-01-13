from .models import Posts, Messages
from  django.forms import ModelForm, TextInput, Select, Textarea
import account.forms


class PostForm(ModelForm):
    class Meta:
        model = Posts
        # fields = '__all__'
        fields = ['title_post', 'text_post', 'category_post', 'author']
        widgets = {
            'title_post': TextInput(attrs={
                'placeholder': 'Заголовок'
                }),
            'text_post': Textarea(attrs={
                'placeholder': 'Текст объявления'
                }),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['text_message',]
        widgets = {
                'text_message': Textarea(attrs={
                    'rows': 1,
                    "class": "form-control",
                    'placeholder': '...',
                    }
                ),
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class SignupForm(account.forms.SignupForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
