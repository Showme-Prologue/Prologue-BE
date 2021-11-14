from django.db import models

from group.models import Group

# Create your models here.

class Question(models.Model):
    group_code = models.ForeignKey(Group, on_delete=CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_code} - {self.question[:100]}"