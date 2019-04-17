from django.db import models
import datetime
from authapp.models import User


class Project(models.Model):  # проект

    slug = models.SlugField(blank=True)
    users = models.ManyToManyField(User, verbose_name='участники')  # , on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название проекта', max_length=128)
    description = models.TextField(verbose_name='опсиание проекта', blank=True)
    date_start = models.DateField(verbose_name='дата начала проекта', default=datetime.date.today())
    date_end = models.DateField(verbose_name='дата окнчания проекта')
    is_active = models.BooleanField(verbose_name='активен', default=True)


class Stage(models.Model):  # этап проекта

    id_project = models.ForeignKey(Project, verbose_name='название проекта', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название этапа', max_length=128)
    description = models.TextField(verbose_name='опсиание этапа', blank=True)
    date_start = models.DateField(verbose_name='дата начала этапа', default=datetime.date.today())
    date_end = models.DateField(verbose_name='дата окнчания этапа')
    status = models.BooleanField(verbose_name='завершен', default=False)
    is_active = models.BooleanField(verbose_name='активен', default=True)


class Task(models.Model):  # задача

    id_project = models.ForeignKey(Project, verbose_name='название проекта', on_delete=models.CASCADE)
    id_stage = models.ForeignKey(Stage, verbose_name='название этапа', on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, verbose_name='исполнители', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название задачи', max_length=128)
    description = models.TextField(verbose_name='опсиание задачи', blank=True)
    date_start = models.DateField(verbose_name='дата начала задачи', default=datetime.date.today())
    date_end = models.DateField(verbose_name='дата окнчания задачи')
    status = models.BooleanField(verbose_name='завершена', default=False)
    is_active = models.BooleanField(verbose_name='активена', default=True)
