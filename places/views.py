from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place, Image


def show_map(request):
    places = Place.objects.filter()
    place_on_map = []
    for place in places:
        place_on_map_template = {
            'type': 'Feature',
            'geometry': {
              'type': 'Point',
              'coordinates': [place.lng, place.lat]
            },
            'properties': {
              'title': place.title,
              'placeId': place.id,
              'detailsUrl': reverse('place-detail', kwargs={'id': place.id})
            }
        }

        place_on_map.append(place_on_map_template)

    places_on_map = {
      'type': 'FeatureCollection',
      'features': place_on_map
    }

    data = {'places': places_on_map}
    return render(request, 'index.html', context=data)


def show_place(request, id=1):
    place = get_object_or_404(Place.objects.prefetch_related(), id=id)
    images = place.images.filter(place_id=id)
    imgs = [image.image.url for image in images]
    response = JsonResponse({
      'title': place.title,
      'imgs': imgs,
      'short_description': place.short_description,
      'long_description': place.long_description,
      'coordinates': {
        'lng': place.lng,
        'lat': place.lat
        }
      },
      safe=False, json_dumps_params={
          'ensure_ascii': False, 'indent': 2
          }
      )
    return response
