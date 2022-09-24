from django.urls import path
from . import views


app_name = 'linkedtask'


urlpatterns = [
    path('', views.linkedtaskIndex, name='linked_tasks'),
    path('add/', views.add_linked_task, name='add_linked_task'),
    path('<int:pk>/', views.linked_task_detail, name='linked_task_detail'),
    path('<int:pk>/update/', views.update_linked_task, name='update_linked_task'),
    path('<int:pk>/delete/', views.delete_linked_task, name='delete_linked_task'),
    path('<int:pk>/tasks/', views.taskIndex, name='tasks'),
    path('<int:pk>/tasks/add/', views.NewTask.as_view(), name='add_task'),
    path('<int:pk>/tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('<int:pk>/tasks/<int:id>/update/', views.update_task, name='update_task'),
    path('<int:pk>/tasks/<int:id>/delete/', views.delete_task, name='delete_task'),
    path('<int:pk>/tasks/<int:id>/entries/', views.task_notes, name='task_entries'),
    path('<int:pk>/tasks/<int:id>/entries/add/', views.add_entry, name='add_entry'),
    path('<int:pk>/tasks/<int:id>/entries/<int:ix>/', views.entry_detail, name='entry_detail'),
    path('<int:pk>/tasks/<int:id>/entries/<int:ix>/update/', views.update_entry, name='update_entry'),
    path('<int:pk>/tasks/<int:id>/entries/<int:ix>/delete/', views.delete_entry, name='delete_entry'),
    path('<int:pk>/attachs/', views.lt_attachments, name='lt_attachments'),
    path('<int:pk>/attachs/add/', views.add_attachment, name='add_attach'),
    path('<int:pk>/attachs/<int:id>/', views.attached_details, name='ltattached_detail'),
    path('<int:pk>/attachs/<int:id>/update/', views.update_attachment, name='update_attach'),
    path('<int:pk>/attachs/<int:id>/delete/', views.delete_attachment, name='delete_attach')

]
