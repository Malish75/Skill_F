from django.forms import ModelForm, BooleanField
from .models import Product


# Создаём модельную форму
class ProductForm(ModelForm):
    check_box = BooleanField(label='Все проверил')  # добавляем галочку, или же true-false поле
    # в класс мета как обычно надо написать модель по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'quantity', 'description',
                  'check_box',
                  ]



'''создание форм - пример'''
# from django.forms import Form, CharField, IntegerField, EmailField
# class DummyForm(Form):
#     field1 = CharField()
#     field2 = IntegerField()
#     field3 = EmailField()