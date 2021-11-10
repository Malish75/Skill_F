from django.shortcuts import render, redirect, reverse
from .models import User, Posts, Messages
from .forms import PostForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView


class PostList(ListView):
    model = Posts  # указываем модель, объекты которой мы будем выводить
    template_name = 'boardapp/index.html'
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к с
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(DetailView):
    model = Posts
    template_name = 'boardapp/detail.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





def create(request):
    error = ''
    # author = User.objects.get(id=self.request.user.id).id
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка при заполнении формы"

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'boardapp/create.html', context)