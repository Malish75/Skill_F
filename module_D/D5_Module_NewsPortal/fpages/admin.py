'''Ну и напоследок хотелось бы отметить, что несмотря на то, что после выполнения миграций,
 в админке появились наши модели FlatPages и Sites, в них по умолчанию зарегистрированы не
  все поля. Для того, чтобы мы могли видеть такие поля, как «Позволить комментировать» или
   «Отображение только зарегистрированным пользователям», нам надо зарегистрировать класс,
    наследуемый от FlatPageAdmin, и добавить в него нужные нам поля '''

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a newapp FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)