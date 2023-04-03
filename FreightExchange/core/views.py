from django.http import HttpResponse
from django.shortcuts import render

from .models import GeoLocations,Freights

# Create your views here.
def freight(request):
    # получаем из данных запроса POST отправленные через форму данные
    fromloc = request.GET.get("fromTxt")
    toloc = request.GET.get("toTxt")

    try:
        fromId=GeoLocations.objects.get(GeoLocationName=fromloc)
    except GeoLocations.DoesNotExist:
        fromId = None

    try:
        toId = GeoLocations.objects.get(GeoLocationName=toloc)
    except GeoLocations.DoesNotExist:
        toId=None
    freights=Freights.objects.all()


    geoloc = GeoLocations.objects.all()

    return render(request, "index.html", {'geoloc': geoloc ,'freights':freights})
