from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit', views.editor, name='editor'),
    path('signup', views.signup, name='signup'),
    path('clear', views.cleartable, name='clear'),
    path('roll', views.rollback, name='roll'),
]