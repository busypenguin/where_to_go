from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Place, Image


def show_map(request):
    places = Place.objects.filter()
    place_on_map = []
    for place in places:
        place_on_map_template = {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [place.lng, place.lat]
            },
            "properties": {
              "title": place.title,
              "placeId": place.id,
              "detailsUrl": f'./places/{place.id}'
            }
        }

        place_on_map.append(place_on_map_template)

    places_on_map = {
      "type": "FeatureCollection",
      "features": place_on_map
    }

    data = {'places': places_on_map}
    return render(request, 'index.html', context=data)


def show_place(request, id=1):
    place = get_object_or_404(Place, id=id)
    images = Image.objects.filter(place_id=id)
    img = []
    for image in images:
        img.append(image.image.url)
    response = JsonResponse({'title': place.title,
                             'imgs': img,
                             "short_description": place.short_description,
                             "long_description": place.long_description,
                             "coordinates": {
                                "lng": place.lng,
                                "lat": place.lat}},
                            safe=False, json_dumps_params={
                                'ensure_ascii': False, 'indent': 2})
    return response
