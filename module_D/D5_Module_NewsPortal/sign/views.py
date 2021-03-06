from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from newapp.models import Author

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    # success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='Authors')
    if not request.user.groups.filter(name='Authors').exists():
        premium_group.user_set.add(user)
    # if not request.objects.filter(user=user).exists():
    #     Author.objects.create(name=user.username, user=user)
    return redirect('/')