from django.db import models


class Place(models.Model):
    place = models.CharField(max_length=200)

    def __str__(self):
        if self.place:
            return self.place


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        if self.image:
            return f'{self.number}  {self.place}'
