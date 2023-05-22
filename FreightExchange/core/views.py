from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddFreight
from django.core.exceptions import ObjectDoesNotExist
from datetime import date

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

    addfr = AddFreight()
    if request.method == "POST":

        form = AddFreight(request.POST)
        if form.is_valid():
            fromloc=request.POST.get("FromLoc")
            toloc=request.POST.get("ToLoc")
            weight=request.POST.get("Weight")
            comment=request.POST.get("Comment")
            contact=request.POST.get("Contact")

            try:
                fromLocation=GeoLocations.objects.get(GeoLocationName=fromloc)
                toLocation=GeoLocations.objects.get(GeoLocationName=toloc)
                fr=Freights(FromLoc=fromLocation,ToLoc=toLocation,Weight=weight,Comment=comment,SubmitedDate=date.today(),Contact=contact,Active=False)
                fr.save()
                message = "Данные благополучно добавились, после подтверждения администратором появится на сайте"
            except ObjectDoesNotExist:
                message="Введенные геоданные нет в базе"
                return render(request,"addfreight.html",{"addfr":addfr,"message": message})

        else:
            message="Попробуйте заново"

    return render(request, "addfreight.html",{"addfr":addfr,"message":message,"fromloc":fromloc,"toloc":toloc,"weight":weight,"comment":comment,"contact":contact, 'fromid':fromLocation})