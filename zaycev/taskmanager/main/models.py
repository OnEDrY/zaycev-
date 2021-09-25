from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Clinic(models.Model):
    name = models.CharField('Название клиники', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'