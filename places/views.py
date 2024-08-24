from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def show_map(request):
    place_moscow_legends = Place.objects.get(title='Экскурсионная компания «Легенды Москвы»')
    moscow_legends = {
        "title": place_moscow_legends.title,
        "imgs": [
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
        ],
        "description_short": place_moscow_legends.description_short,
        "description_long": place_moscow_legends.description_long,
        "coordinates": {
            "lng": place_moscow_legends.lng,
            "lat": place_moscow_legends.lat
        }
    }
    place_roofs24 = Place.objects.get(title="Экскурсионный проект «Крыши24.рф»")
    roofs24 = {
        "title": place_roofs24.title,
        "imgs": [
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/af7b8599fec9d2542a011f1d01d459e2.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/965c5a3ff5b2431e646d30b6744afd2d.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/06868b2b01ff8db506cd21956a6cb636.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a8cc3e03f56413275ded99e51226a70f.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/44e96733303e7490aaa1cf2eebfbbfff.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/fadf618505b087fa539e883f33f850b2.jpg",
            "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/ec461a89a1d0d5a4cb7c81f1fc0a4e89.jpg"
        ],
        "description_short": place_roofs24.description_short,
        "description_long": place_roofs24.description_long,
        "coordinates": {
            "lng": place_roofs24.lng,
            "lat": place_roofs24.lat
        }
    }
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
            "detailsUrl": moscow_legends
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
            "detailsUrl": roofs24
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
                             'img': img,
                             "description_short": place.description_short,
                             "description_long": place.description_long,
                             "coordinates": {
                                "lng": place.lng,
                                "lat": place.lat}},
                            safe=False, json_dumps_params={
                                'ensure_ascii': False, 'indent': 2})
    return response
