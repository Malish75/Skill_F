from datetime import datetime
from .filters import PostFilter  #, SearchFilter
from .models import Post, Category
from .forms import PostForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from django.core.paginator import Paginator
from django.shortcuts import render


class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к с
    # queryset = Post.objects.order_by('-id') # переопределенная сортировка
    ordering = ['-id'] # сортировка от свежей новости к старой, свежие в начале
    paginate_by = 10
    form_class = PostForm

    # метод get_context_data нужен для того, чтобы передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные.
    # Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        # context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        context['all_posts'] = len(Post.objects.all()) # количество постов, передаваемых в шаблон
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)


# дженерик для получения деталей новости
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()
    # context_object_name = 'news_detail'
    #
#
# # дженерик для создания объекта.
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm

# #
# # для поиска публикаций
class PostSearchView(PostsList):
    template_name = 'post_search.html'
    paginate_by = 10


# # дженерик для редактирования объекта
class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
#
#
# дженерик для удаления
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'







