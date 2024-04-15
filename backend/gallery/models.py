from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'gallery'  # Explicitly specify the app_label for the model