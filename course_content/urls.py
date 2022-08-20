from unicodedata import name
from django.urls import path 
from . import views


urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('create-course/', views.create_course, name='create-course'),   
    path('create-tag/', views.create_tag, name='create_tag'),
    path('create-lesson/<int:pk>/', views.create_lesson, name='create-lesson'),
]
