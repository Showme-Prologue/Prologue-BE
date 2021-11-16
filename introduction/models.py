from django.db import models

from group.models import Group

# Create your models here.

class Introduction(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_code = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, default='media/default.png', upload_to="uploads")

    def __str__(self):
        return f"{self.id} / {self.group_code}"

class IntroductionQuestion(models.Model):
    group_code = models.ForeignKey(Group, on_delete=models.CASCADE)
    question = models.TextField()
    is_updated = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.group_code} - {self.question[:50]}"

class IntroductionComponent(models.Model):
    introduction_id = models.ForeignKey(Introduction, related_name='qna', on_delete=models.CASCADE)
    sequence = models.PositiveIntegerField()
    question_id = models.ForeignKey(IntroductionQuestion, related_name='questions', on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f"{self.question_id} - {self.answer[:30]}"