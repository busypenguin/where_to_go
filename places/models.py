from django.db import models


class Place(models.Model):
    place = models.CharField(max_length=200)

    def __str__(self):
        if self.place:
            return self.place
