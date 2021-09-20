from django.urls import path
from . import views


app_name = 'knowledgebase'


urlpatterns = [
    path('', views.kb_index, name='kb_entries'),
    path('add/', views.add_kb, name='add_kb'),
    path('<int:pk>/', views.kb_detail, name='kb_detail'),
    path('<int:pk>/update/', views.update_kb, name='update_kb'),
    path('<int:pk>/delete/', views.delete_kb, name='delete_kb'),
    path('<int:pk>/attachs/', views.kb_attachments, name='kb_attachments'),
    path('<int:pk>/attachs/add/', views.add_attachment, name='add_attachment'),
    path('<int:pk>/attachs/<int:id>/', views.attached_details, name='attached_detail'),
    path('<int:pk>/attachs/<int:id>/update/', views.update_attachment, name='update_attached'),
    path('<int:pk>/attachs/<int:id>/delete/', views.delete_attachment, name='delete_attached')
]
