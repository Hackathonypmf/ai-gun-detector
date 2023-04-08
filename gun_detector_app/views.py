from django.shortcuts import render, redirect
from django.views import View
from .models import Video
from .forms import VideoUploadForm
from .gun_detection import detect_guns

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class VideoUploadView(View):
    def get(self, request):
        form = VideoUploadForm()
        return render(request, 'video_upload.html', {'form': form})

    def post(self, request):
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect('gun_detection', video_id=video.id)
        return render(request, 'video_upload.html', {'form': form})

class GunDetectionView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        video.detected_guns = detect_guns(video.file.path)
        video.save()
        return redirect('video_results', video_id=video.id)

class VideoResultsView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        detected_guns = video.detected_guns.split(',')
        return render(request, 'video_results.html', {'video': video, 'detected_guns': detected_guns})
