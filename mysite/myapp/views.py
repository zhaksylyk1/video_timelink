from django.shortcuts import render, redirect, get_object_or_404
from .forms import VideoForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'myapp/upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()  # Fetch all video objects from the database
    time_points = [('Intro', 10), ('Middle', 30), ('End', 40)]
    return render(request, 'myapp/video_list.html', {'videos': videos, 'time_points': time_points})

def delete_video(request, video_id):
    if request.method == 'POST':  # Ensure the request method is POST
        video = Video.objects.get(id=video_id)  # Get the video to delete
        video.delete()  # Delete the video
        return redirect('video_list')  # Redirect to the video list page


