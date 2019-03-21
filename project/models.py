from django.db import models
from django.utils.timezone import now
# from auth_app.models import User  # модели пока нет, как и приложения auth_app


class Project(models.Model):  # проект

    slug = models.SlugField(unique=True)
    # users = models.ManyToManyField(User, verbose_name='участники', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название проекта', max_length=128, unique=True)
    description = models.TextField(verbose_name='опсиание проекта', blank=True)
    date_start = models.DateTimeField(verbose_name='дата начала проекта', default=now())
    date_end = models.DateTimeField(verbose_name='дата окнчания проекта')
    is_active = models.BooleanField(verbose_name='активен', default=True)

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.is_active = False
    #     self.object.save()


class Stage(models.Model):  # этап проекта

    id_project = models.ForeignKey(Project, verbose_name='название проекта', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название этапа', max_length=128, unique=True)
    description = models.TextField(verbose_name='опсиание этапа', blank=True)
    date_start = models.DateTimeField(verbose_name='дата начала этапа', default=now())
    date_end = models.DateTimeField(verbose_name='дата окнчания этапа')
    status = models.BooleanField(verbose_name='завершен', default=False)
    is_active = models.BooleanField(verbose_name='активен', default=True)


class Task(models.Model):  # задача

    id_project = models.ForeignKey(Project, verbose_name='название проекта', on_delete=models.CASCADE)
    id_stage = models.ForeignKey(Stage, verbose_name='название этапа', on_delete=models.CASCADE)
    # id_user = models.ForeignKey(User, verbose_name='исполнители', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='название задачи', max_length=128, unique=True)
    description = models.TextField(verbose_name='опсиание задачи', blank=True)
    date_start = models.DateTimeField(verbose_name='дата начала задачи', default=now())
    date_end = models.DateTimeField(verbose_name='дата окнчания задачи')
    status = models.BooleanField(verbose_name='завершена', default=False)
    is_active = models.BooleanField(verbose_name='активена', default=True)
