from django.core.management.base import BaseCommand
import os
import django
from places.models import Place, Image
import requests
from django.core.files.base import ContentFile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "where_to_go.settings")
django.setup()


class Command(BaseCommand):
    help = 'Load places to DB'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(url=options['url'])
        serialized_place = response.json()
        place, _ = Place.objects.get_or_create(
            title=serialized_place['title'],
            description_short=serialized_place['description_short'],
            description_long=serialized_place['description_long'],
            lng=serialized_place['coordinates']['lng'],
            lat=serialized_place['coordinates']['lat']
        )
        images = serialized_place['imgs']
        for index, img in enumerate(images):
            resp = requests.get(img)
            image, _ = Image.objects.get_or_create(place=place, number=index)
            image.image.save(str(img), ContentFile(resp.content), save=True)
