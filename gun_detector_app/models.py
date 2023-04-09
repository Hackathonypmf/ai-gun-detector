from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    detected_guns = models.TextField(blank=True, null=True)
    keypoints_gif = models.FileField(upload_to='keypoints_gifs/', null=True, blank=True)

    def __str__(self):
        return self.title