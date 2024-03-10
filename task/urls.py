from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_Task, name='task' ),
    path('edit/<int:id>',views.edit_task,name='edit_task'),
]
