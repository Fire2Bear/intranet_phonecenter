# Import
from django.utils.translation import gettext as _
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, AccountSettingsForm
from .models import UserProfile


# Views
def hello_old(request):
    return HttpResponse("Hello Wolrd !")


def hello(request):
    return render(
        request,
        'users/hello.html',
        {
            'message': _("Hello Wolrd !"),
        }
    )


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:hello"))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            raw_password = form.cleaned_data['raw_password']
            user = UserProfile.objects.create_user(
                username=username,
                email=email,
                password=raw_password,
            )
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse("users:hello"))
    else:
        form = RegisterForm()
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("users:register"),  # par défaut renvoie vers lui même
            'title': "Inscription",
            'form': form,
        })


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:hello"))
    elif 'username' in request.POST and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next') is not None:
                return redirect(request.GET['next'])
            else:
                return HttpResponseRedirect(reverse("users:hello"))
        else:
            return render(
                request,
                'users/login.html',
                {
                    "auth_error": True,
                }
            )
    else:
        return render(
            request,
            'users/login.html',
            {}
        )


@login_required
def myaccount(request):
    return render(
        request,
        'users/myaccount.html',
    )


# Ajouter cette view
@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountSettingsForm(instance=request.user)
    return render(
        request,
        'utils/form.html',
        {
            'url_form': reverse("users:register"),
            'title': "Inscription",
            'form': form,
        }
    )
