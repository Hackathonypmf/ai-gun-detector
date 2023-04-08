"""gun_detector_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gun_detector_app import views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),path('upload-video/', views.VideoUploadView.as_view(), name='upload-video'),
# ]
# from .views import VideoUploadView, GunDetectionView, VideoResultsView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('upload/', views.VideoUploadView.as_view(), name='upload_video'),
    path('detect/<int:video_id>/', views.GunDetectionView.as_view(), name='gun_detection'),
    path('results/<int:video_id>/', views.VideoResultsView.as_view(), name='video_results'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)