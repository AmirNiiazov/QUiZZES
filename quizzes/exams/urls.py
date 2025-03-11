from django.urls import path
from . import views

urlpatterns = [
    path('create_exam/', views.create_exam, name='create_exam'),
    path('add_question/<int:exam_id>/', views.add_question, name='add_question'),
    path('add_answer/<int:question_id>/', views.add_answer, name='add_answer'),
]