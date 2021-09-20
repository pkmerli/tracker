from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.TD_index, name='todo'),
    path('add/', views.add_todo, name='add_todo'),
    path('<int:pk>/', views.td_detail, name='todo_detail'),
    path('<int:pk>/attachs/', views.get_task_attachments, name='task_attachments'),
    path('<int:pk>/attachs/add/', views.add_attachment, name='add_attach'),
    path('<int:pk>/attachs/<int:id>/', views.attached_details, name='attached_detail'),
    path('<int:pk>/attachs/update/<int:id>/', views.update_attachment, name='update_attached'),
    path('<int:pk>/attachs/delete/<int:id>/', views.delete_attachment, name='delete_attached'),
    path('update/<int:pk>/', views.td_update, name='update_todo'),
    path('delete/<int:pk>/', views.DeleteToDo.as_view(), name='delete_todo')
]
