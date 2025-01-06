from django.db import models
from datetime import datetime

class Account(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Post(models.Model):
    account = models.ForeignKey(Account, related_name='posts', on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    content_type = models.CharField(max_length=50)  # Тип поста (например, текстовый, фото, видео и т.д.)

    def __str__(self):
        return f"Post by {self.account.username} on {self.post_date}"