from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # пользователь

    name = models.CharField(verbose_name='имя', max_length=128, unique=True)
    position = models.CharField(verbose_name='должность', max_length=128, blank=True)
    email = models.EmailField(verbose_name='Электронная почта пользователя', blank=True, unique=True)
    role = models.CharField(verbose_name='Роль пользователя', max_length=128, blank=True)
    avatar = models.ImageField(verbose_name='Аватар пользователя', blank=True)
    is_active = models.BooleanField(verbose_name='активен', default=True)

