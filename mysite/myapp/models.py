from django.db import models

# Create your models here.
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True) 
    # Optionally, add more fields such as description, timestamps, etc.
    
