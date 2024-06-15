from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    """
    This model for Register User Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Messages(models.Model):
    """
    This model for Messages
    """
    sender = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='messages/photo/', blank=True, null=True,
                             validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'], message='Photo')])
    video = models.FileField(upload_to='messages/video/', blank=True, null=True,
                             validators=[FileExtensionValidator(['mp4', 'mov', 'avi'], message='Video')])
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.receiver} : {self.text}'


class Friend(models.Model):
    """
    This model for Friends
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='login_user')
    friend = models.ManyToManyField(User)

    def __str__(self):
        return self.user.name


