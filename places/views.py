from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def show_map(request):
    place_moscow_legends = Place.objects.get(title='Экскурсионная компания «Легенды Москвы»')
    place_roofs24 = Place.objects.get(title="Экскурсионный проект «Крыши24.рф»")
    places = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place_moscow_legends.lng, place_moscow_legends.lat]
          },
          "properties": {
            "title": "«Легенды Москвы»",
            "placeId": "moscow_legends",
            "detailsUrl": './places/1'
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place_roofs24.lng, place_roofs24.lat]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": './places/2'
          }
        }
      ]
    }
    data = {'places': places}
    return render(request, 'index.html', context=data)


def show_place(request, id=1):
    place = get_object_or_404(Place, id=id)
    images = Image.objects.filter(place_id=id)
    img = []
    for image in images:
        img.append(image.image.url)
    response = JsonResponse({'title': place.title,
                             'imgs': img,
                             "description_short": place.description_short,
                             "description_long": place.description_long,
                             "coordinates": {
                                "lng": place.lng,
                                "lat": place.lat}},
                            safe=False, json_dumps_params={
                                'ensure_ascii': False, 'indent': 2})
    return response
