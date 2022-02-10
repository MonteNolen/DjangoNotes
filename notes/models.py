from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

POST_CHOICES = (
    ('o', 'Оператор'),
    ('i', 'Ведущий инженер'),
    ('a', 'Администратор')

)
class NoteAuthor(models.Model):
    """
    Модель представляющая автора.
    """
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)

    post = models.CharField(max_length=1, choices=POST_CHOICES, default="Оператор", verbose_name="Должность")
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return '{0} {1}'.format (self.name, self.surname)

class Note(models.Model):
    """
    Модель для представления отчета
    """
    title = models.CharField("Заголовок", max_length=100)
    user = models.ForeignKey('NoteAuthor', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь')
    created = models.DateField("Создана", auto_now=True)
    status = models.BooleanField("Закрыто?", default=False)
    textarea = HTMLField("Поле для отчета", max_length=1000)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])