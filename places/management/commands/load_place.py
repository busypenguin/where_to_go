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

    def add_arguments(self, parser):
        parser.add_argument('path_to_json', type=str, help='Путь до json файла')

    def handle(self, *args, **options):
        path_to_json = options['path_to_json']
        requested_path_to_json = requests.get(path_to_json)
        requested_path_to_json.raise_for_status()
        serialized_place = requested_path_to_json.json()
        if 'error' in serialized_place:
            raise requests.exceptions.HTTPError(serialized_place['error'])

        try:
            place = Place.objects.get(
                title=serialized_place['title'],
                short_description=serialized_place['description_short'],
                long_description=serialized_place['description_long'],
                lng=serialized_place['coordinates']['lng'],
                lat=serialized_place['coordinates']['lat']
            )
        except Place.DoesNotExist:
            place = Place.objects.create(
                title=serialized_place['title'],
                short_description=serialized_place['description_short'],
                long_description=serialized_place['description_long'],
                lng=serialized_place['coordinates']['lng'],
                lat=serialized_place['coordinates']['lat']
            )
        images = serialized_place['imgs']
        for index, img in enumerate(images):
            resp = requests.get(img)
            resp.raise_for_status()
            Image.objects.create(place=place, image=ContentFile(resp.content, str(img)), number=index)