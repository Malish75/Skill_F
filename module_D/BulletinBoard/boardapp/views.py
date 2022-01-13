from django.shortcuts import render, redirect, reverse
from .models import User, Posts, Messages
from .forms import PostForm, MessageForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User
import account.forms
import boardapp.forms
import account.views


class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):
    form_class =  boardapp.forms.SignupForm

    def generate_username(self, form):
        username = form.cleaned_data["email"]
        return username

    def after_signup(self, form):
        # do something
        super(SignupView, self).after_signup(form)



class PostList(ListView):
    model = Posts  # указываем модель, объекты которой мы будем выводить
    template_name = 'boardapp/index.html'
    context_object_name = 'get_post'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к с
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):          # подсветка строки с измененниями
        return '%s?id=%s'% (self.success_url, self.object.id)


class PostDetailView(CustomSuccessMessageMixin, FormMixin, DetailView):
    model = Posts
    template_name = 'boardapp/detail.html'
    context_object_name = 'get_post'
    form_class = MessageForm
    success_msg = "Отклик создан, ожидайте модерации."

    def get_success_url(self, **kwargs):
        return  reverse_lazy('post_detail', kwargs={'pk':self.get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class PostCreate(CustomSuccessMessageMixin, CreateView):
    model = Posts
    template_name = 'boardapp/create.html'
    form_class = PostForm

    context_object_name = 'get_post'

    success_url = reverse_lazy('home')
    success_msg = "Запись успешно создана."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)








class PostUpdate(CustomSuccessMessageMixin, UpdateView):
    model = Posts
    template_name = 'boardapp/create.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_msg = "Изменения успешно внесены."

    def get_context_data(self, **kwargs):
        kwargs['success_update'] = True
        return super().get_context_data(**kwargs)


class PostDelete(CustomSuccessMessageMixin, DeleteView):
    model = Posts
    template_name = 'boardapp/create.html'
    success_url = reverse_lazy('home')
    success_msg = "Объявление успешно удалено."

    def post(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)







# def delete_page(request, pk):
#     get_post = Posts.objects.get(pk=pk)
#     get_post.delete()
#     return redirect(reverse("home"))


# def post_create(request):
#     success = False
#     error = ''
#     # author = User.objects.get(id=self.request.user.id).id
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True
#             return redirect('home')
#         else:
#             error = "Ошибка при заполнении формы"
#     form = PostForm()
#     context = {
#         'form': form,
#         'error': error,
#         'success': success,
#     }
#     return render(request, 'boardapp/create.html', context)


# def update_page(request, pk):
#     success_update = False
#     template = 'boardapp/create.html'
#     get_post = Posts.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=get_post)
#         if form.is_valid():
#             form.save()
#             success_update = True
#     context = {
#                 'get_post': get_post,
#                 'update': True,
#                 'form': PostForm(instance=get_post),
#                 'success_update': success_update,
#             }
#     return render(request, template, context, )
