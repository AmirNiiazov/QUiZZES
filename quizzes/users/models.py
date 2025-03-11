from django.contrib.auth.models import User
from django.db import models


# Модель профиля пользователя (с дополнительной информацией)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    completed_tests_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"