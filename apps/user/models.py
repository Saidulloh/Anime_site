from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    photo = models.ImageField(
        upload_to='user_photo/',
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=15,
        choices=GENDER_CHOICES
    )
    birthday = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.username}'