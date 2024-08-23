from django.db import models


class Place(models.Model):
    title = models.CharField(blank=True, max_length=200)
    description_short = models.CharField(blank=True, max_length=300)
    description_long = models.TextField(blank=True)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        if self.title:
            return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        if self.image:
            return f'{self.number}  {self.place}'
