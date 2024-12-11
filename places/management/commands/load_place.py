import os
import json
from io import BytesIO
from PIL import Image as PILimage
import requests
import django

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places to DB'

    def handle(self, *args, **options):
        path = 'places/places'
        for dirs, folder, files in os.walk(path):
            for file in files:
                with open(f'{dirs}/{file}') as f:
                    serialized_place = json.load(f)
                    place, _ = Place.objects.get_or_create(
                        title=serialized_place['title'],
                        short_description=serialized_place['description_short'],
                        long_description=serialized_place['description_long'],
                        lng=serialized_place['coordinates']['lng'],
                        lat=serialized_place['coordinates']['lat']
                    )
                    images = serialized_place['imgs']
                    for index, img in enumerate(images):
                        resp = requests.get(img)
                        image, _ = Image.objects.get_or_create(place=place, number=index)
                        image.image.save(str(img), ContentFile(resp.content), save=True)