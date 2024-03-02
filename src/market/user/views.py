from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate


def user_register(request):
    print(request.method)
    print(request.POST)
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        print(form, form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def user_login(request):
    form = LoginForm()

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            print(user)

    context = {
        "form": form
    }
    return render(request, 'login.html', context)
