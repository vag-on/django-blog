from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    bodypost = models.TextField('Текст')
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    
    def __str__(self):
        return f'{self.title}, {self.author}'
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
