
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render,redirect
from .models import Anime
from .forms import AddAnimeForm
from django.contrib.auth import login
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request,'anime/index.html')


def animes(request):
    user = request.user
    animes = Anime.objects.filter(user=user)
    context = {
        'animes':animes,
    }
    return render(request,'anime/animes.html',context)


def add_anime(request):
    if request.method == "POST":
       form = AddAnimeForm(data=request.POST)
       user = request.user
       if form.is_valid():
        anime = form.save(commit=False)
        anime.user = user
        anime.save()
        return redirect('anime:add_anime')  # например, 'animes'

    else:
        form = AddAnimeForm()
    
    context = {
        'form':form,
    }
    return render(request,'anime/add_anime.html',context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('anime:index')  # или куда хотите
    else:
        form = RegisterForm()
    return render(request, 'anime/register.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('anime:index')  # или ваше название главной страницы
            else:
                messages.error(request, 'Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'anime/login.html', {'form': form})