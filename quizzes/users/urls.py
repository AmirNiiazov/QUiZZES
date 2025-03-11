from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_user_exam/<int:user_exam_id>/', views.delete_user_exam, name='delete_user_exam'),
]