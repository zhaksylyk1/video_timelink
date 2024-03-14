from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),  # For listing videos
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),  # URL pattern for the delete view
    # path('upload/', views.upload_video, name='upload_video'),  # For uploading videos
   
]
