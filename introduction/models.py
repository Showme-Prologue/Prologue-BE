from django.db import models

from account.models import User
from group.models import Group

# Create your models here.

class Introduction(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    groupCode = models.ForeignKey(Group, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, default='media/default.png', upload_to="uploads")

    def __str__(self):
        return f"{self.id} / {self.groupCode}"

class IntroductionQuestion(models.Model):
    groupCode = models.ForeignKey(Group, on_delete=models.CASCADE)
    question = models.TextField()
    isUpdated = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.groupCode} - {self.question[:50]}"

class IntroductionComponent(models.Model):
    introductionId = models.ForeignKey(Introduction, related_name='qna', on_delete=models.CASCADE)
    sequence = models.PositiveIntegerField()
    questionId = models.ForeignKey(IntroductionQuestion, related_name='questions', on_delete=models.CASCADE)
    answer = models.TextField()
    isSimpleInfo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.questionId} - {self.answer[:30]}"