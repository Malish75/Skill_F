from datetime import datetime
from .filters import PostFilter
from .forms import PostForm, CommentForm
from .models import Post, Category, Comment, PostCategory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse


class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к с
    # queryset = Post.objects.order_by('-id') # переопределенная сортировка
    ordering = ['-id'] # сортировка от свежей новости к старой, свежие в начале
    paginate_by = 10
    form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

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

    # def get_context_data(self, *args, **kwargs):
    #     return {
    #         **super().get_context_data(*args, **kwargs),
    #         'filter': self.get_filter(),
    #         'form': self.form_class,
    #         'all_post': Post.objects.all(),
    #         'time_now': datetime.utcnow(),
    #         'is_not_authors': not self.request.user.groups.filter(name='authors').exists(),
    #         'all_category': Category.objects.filter(),
    #     }
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)


# дженерик для получения деталей новости
class PostDetailView(PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    permission_required = ('newapp.add_post',)
    # form_class = CommentForm

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        try:
            # context['CP'] = Comment.objects.filter(post=self.kwargs['pk'])
            context['PCC'] = PostCategory.objects.get(post=self.kwargs['pk']).category
            context['all_category'] = Category.objects.get(post=self.kwargs.get('pk'))
            # context['time'] = datetime.utcnow()
            context['is_subscriber'] = Category.objects.get(post=self.kwargs.get('pk')).subscriber.filter(username=self.request.user).exists()

        except Comment.DoesNotExist:
            context['CP'] = None
            context['PCC'] = None
            context['all_category'] = None
        return context

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.get_object().id})

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)
    #
    # def form_valid(self, form):
    #     comment = form.save(commit=False)
    #     comment.post = self.get_object()
    #     comment.user = self.request.user
    #     comment.save()
    #     return super().form_valid(form)


# дженерик для создания объекта.
class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    context_object_name = 'posts'
    permission_required = 'newapp.add_post'


# для поиска публикаций
class PostSearchView(PostsList):
    template_name = 'post_search.html'
    paginate_by = 10


# дженерик для редактирования объекта
class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    permission_required = 'newapp.change_post'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = 'newapp.delete_post'


# @login_required
# def subscribe_me(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     if category not in user.category_set.all():
#         # category.subscribers.add(user)
#         category.subscriber.add(user)
#         return redirect(request.META.get('HTTP_REFERER'))
#     else:
#         return redirect(request.META.get('HTTP_REFERER'))
#
#
# @login_required
# def unsubscribe_me(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     if category in user.category_set.all():
#         # category.subscribers.remove(user)
#         category.subscriber.remove(user)
#         return redirect(request.META.get('HTTP_REFERER'))
#     else:
#         return redirect(request.META.get('HTTP_REFERER'))


class Subscriber(UpdateView):
    model = Category

    def post(self, request, *args, **kwargs):
        if not Category.objects.get(pk=self.kwargs.get('pk')).subscriber.filter(username=self.request.user).exists():
            Category.objects.get(pk=self.kwargs.get('pk')).subscriber.add(self.request.user)
        else:
            Category.objects.get(pk=self.kwargs.get('pk')).subscriber.remove(self.request.user)
        return redirect(request.META.get('HTTP_REFERER'))
