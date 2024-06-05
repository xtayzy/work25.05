from django.urls import path

from todo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('done/<int:id>', views.done, name='done'),
    path('notdone/<int:id>', views.notdone, name='notdone')
]