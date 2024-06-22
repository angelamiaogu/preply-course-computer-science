from django.urls import path
from . import views

urlpatterns = [
    path('', views.lessons_list, name='lessons_list'),
    path('<slug:slug>/', views.lesson_detail, name='lesson_detail'),
    path('create/fques/', views.funny_questions, name='funny-questions'),

]
