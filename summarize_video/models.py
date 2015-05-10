from django.db import models

# Create your models here.
class Video(models.Model):
    video_link = models.CharField(max_length=200)

class VisualSummary(models.Model):
    gif_image = models.CharField(max_length=200)

class TextSummary(models.Model):
    text_summary = models.CharField(max_length=200)
