from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    is_banned=models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('profile')
    
    def __str__(self):
        return self.username
# Create your models here