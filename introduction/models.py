from django.db import models

# Create your models here.

class Introduction(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #group_code = models.ForeignKey(Group, on_delete=models.CASCADE)
    #question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer[:100]