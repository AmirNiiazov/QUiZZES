from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Вход пользователя
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Логиним пользователя
            return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


# Профиль пользователя
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправляем обратно на профиль
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'form': form})


# Выход пользователя
def user_logout(request):
    logout(request)
    return redirect('login')
