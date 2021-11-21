from django.db import models

from account.models import User

# Create your models here.

class Group(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    profile_photo = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class GroupUserList(models.Model):
    groupCode = models.ForeignKey(Group, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    isStaff = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.groupCode} - {self.userId.name}"
    