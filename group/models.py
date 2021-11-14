from django.db import models

# Create your models here.

class Group(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    profile_photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"