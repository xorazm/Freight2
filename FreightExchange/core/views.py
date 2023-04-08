from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddFreight

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


def addfreight(request):
    message = ""
    fromloc=""
    toloc=""
    comment=""
    contact=""
    weight=""
    fromid=""
    fromLocation=""
    if request.method == "POST":

        form = AddFreight(request.POST)
        if form.is_valid():
            fromloc=request.POST.get("FromLoc")
            toloc=request.POST.get("ToLoc")
            weight=request.POST.get("Weight")
            comment=request.POST.get("Comment")
            contact=request.POST.get("Contact")
            message="Данные благополучно добавились"
            fromLocation=GeoLocations.objects.get(GeoLocationName=fromloc)

        else:
            message="Попробуйте заново"
    addfr=AddFreight()
    return render(request, "addfreight.html",{"addfr":addfr,"message":message,"fromloc":fromloc,"toloc":toloc,"weight":weight,"comment":comment,"contact":contact, 'fromid':fromLocation})