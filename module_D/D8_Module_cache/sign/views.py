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
    premium_group = Group.objects.get(name='Author')
    if not request.user.groups.filter(name='Author').exists():
        premium_group.user_set.add(user)
        Author.objects.create(author=user)

    return redirect('/')