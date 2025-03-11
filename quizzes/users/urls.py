from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_user, name='login'),  # Страница входа
    path('profile/', views.profile, name='profile'),  # Страница профиля
    path('logout/', views.user_logout, name='logout'),  # Маршрут для выхода
]