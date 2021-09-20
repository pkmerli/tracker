from django.urls import path
from . import views


app_name = 'issues'

urlpatterns = [
    path('', views.bugIndex, name='issues'),
    path('add/', views.add_issue, name='new_bug'),
    path('<int:pk>/', views.bug_detailview, name='bug_detail'),
    path('<int:pk>/notes/', views.bug_notes, name='bug_entries'),
    path('<int:pk>/notes/add/', views.add_entry, name='add_notes'),
    path('<int:pk>/notes/<int:id>/', views.entry_detail, name='bugentry_detail'),
    path('<int:pk>/notes/<int:id>/update/', views.update_entry, name='update_entry'),
    path('<int:pk>/notes/<int:id>/delete/', views.delete_entry, name='delete_entry'),
    path('<int:pk>/attachs/', views.get_bug_attachments, name='bug_attachments'),
    path('<int:pk>/attachs/add/', views.add_attachment, name='add_attached'),
    path('<int:pk>/attachs/<int:id>/', views.attached_details, name='attached_detail'),
    path('<int:pk>/attachs/update/<int:id>/', views.update_attachment, name='update_attached'),
    path('<int:pk>/attachs/delete/<int:id>/', views.delete_attachment, name='delete_attached'),
    path('update/<int:pk>/', views.update_bug, name='update_bug'),
    path('delete/<int:pk>/', views.DeleteBug.as_view(), name='delete_issue')
]
