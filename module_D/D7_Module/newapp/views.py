from .filters import PostFilter
from .forms import PostForm, ContactForm, CommentForm
from .models import Post, Category, Comment, PostCategory, User, Author
from datetime import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, reverse, render



class PostsList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'posts.html'
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к с
    # queryset = Post.objects.order_by('-id') # переопределенная сортировка
    ordering = ['-id']
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
        context['time_now'] = datetime.utcnow()
        # context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        context['categories'] = Category.objects.all()
        context['form'] = PostForm()
        context['all_posts'] = len(Post.objects.all()) # количество постов

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)


# дженерик для получения деталей новости
class PostDetailView(DetailView):
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
            context['is_subscriber'] = Category.objects.get(post=self.kwargs.get('pk')).subscriber.filter(username=self.request.user).exists()
        except Comment.DoesNotExist:
            context['CP'] = None
            context['PCC'] = None
            context['all_category'] = None
        return context

    def get_success_url(self):
        return reverse('news_detail', kwargs={'pk': self.get_object().id})


# дженерик для создания объекта.
class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    context_object_name = 'posts'
    permission_required = 'newapp.add_post'
    daily_post_limit = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        author = User.objects.get(id=self.request.user.id).id # request.user.id - текущий зарег польз-ль  asmal75 --> 35
        author_id_id = Author.objects.get(author_id=author).id   # 35 юзера  -- >  9 автора
        all_posts_self_author = Post.objects.filter(author_id=author_id_id).values('time_in_new_post')  # <QuerySet [{'time_in_new_post': datetime.datetime(2021, 7, 5, 9, 58, 48, 541411, tzinfo=<UTC>)}
        now = datetime.now()
        list_dates_of_author = [item['time_in_new_post'].date() for item in all_posts_self_author if item['time_in_new_post'].date() == now.date()]

        context['publications_for_today_limit'] = self.daily_post_limit - len(list_dates_of_author)

        return context

# print( today.strftime("%m/%d/%Y") )


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

# подписка на категорию новости
class Subscriber(UpdateView):
    model = Category

    def post(self, request, *args, **kwargs):
        if not Category.objects.get(pk=self.kwargs.get('pk')).subscriber.filter(username=self.request.user).exists():
            Category.objects.get(pk=self.kwargs.get('pk')).subscriber.add(self.request.user)
        else:
            Category.objects.get(pk=self.kwargs.get('pk')).subscriber.remove(self.request.user)
        return redirect(request.META.get('HTTP_REFERER'))


######  отправка письма ИЗ ЮТУБА  РАБОТАЕТ!!!!!!!
def test_mail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['content'],
                             'andstamal@yandex.ru',
                             ['asmal75@bk.ru'],
                             fail_silently=False)
            if mail:
                messages.success(request, 'Письмо успешно отправлено')
                return redirect('/news/test/')
            else:
                messages.error(request, 'Ошибка отправки письма')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'test.html', {'form': form})

