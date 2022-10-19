from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.todos, name='todos'),
    path('update/<int:task_id>/',views.update_todo, name='update'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('task-done/<int:id>/',views.mark_completed, name='task-done'),
]