from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True
        )
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True
        )
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    class Meta:
        ordering = ['title']
        unique_together = ['lng', 'lat']

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE
        )
    image = models.ImageField(verbose_name='Изображение')
    number = models.PositiveIntegerField(
        verbose_name='Номер',
        default=0,
        db_index=True,
        blank=True
        )

    class Meta:
        ordering = ['number']

    def __str__(self):
        if self.image:
            return f'{self.number}  {self.place}'
