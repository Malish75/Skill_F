
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # мы получили весь контекст из класса-родителя
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

'''
 Сначала мы получили весь контекст из класса-родителя, а после чего добавили новую контекстную переменную 
 is_no t_premium. Чтобы ответить на вопрос, есть ли пользователь в группе, мы заходим в переменную запроса self.request
  (вспоминаем начало этого модуля). Из этой переменной мы можем вытащить текущего пользователя. В поле groups хранятся
   все группы, в которых он состоит. Далее мы применяем фильтр к этим группам и ищем ту самую, имя которой premium. 
   После чего проверяем, есть ли какие-то значения в отфильтрованном списке. Метод exists() вернет True, если группа
    premium в списке групп пользователя найдена, иначе — False. А нам нужно получить наоборот — True, если пользователь
     не находится в этой группе, по этому добавляем отрицание not. И возвращаем контекст обратно.
'''