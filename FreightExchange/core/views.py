from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import AddFreight
from django.core.exceptions import ObjectDoesNotExist
from datetime import date

from .models import GeoLocations,Freights

#def autocomplete (request):



# Create your views here.
def freight(request):
    if 'term' in request.GET:
        titles = list()
        qs=GeoLocations.objects.filter(GeoLocationName__istartswith =request.GET.get('term').capitalize())

        for geo in qs:
            titles.append(geo.GeoLocationName)
        return JsonResponse(titles, safe=False)

    page = request.GET.get('page', 1)

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


    if toId is not None and fromId is not None:
        toIdChilds=[]
        fromIdChilds=[]

        freights=''
        if fromId is not None:
            fromIdChilds = fromId.get_all_children()

        if toId is not None:
            toIdChilds=toId.get_all_children()

        if len(toIdChilds)==0 and len(fromIdChilds)>0:
            freights=Freights.objects.filter(FromLoc__in=fromIdChilds)
        if len(toIdChilds) > 0 and len(fromIdChilds)== 0:
            freights = Freights.objects.filter(ToLoc__in=toIdChilds)
        if len(toIdChilds) > 0 and len(fromIdChilds)> 0:
            freights = Freights.objects.filter(FromLoc__in=fromIdChilds,ToLoc__in=toIdChilds)
    else:
        freights = Freights.objects.all()




    paginator = Paginator(freights, 3)
    try:
        freights = paginator.page(page)
    except PageNotAnInteger:
        freights = paginator.page(1)
    except EmptyPage:
        freights = paginator.page(paginator.num_pages)




    return render(request, "index.html", {'freights':freights, 'fromloc':fromloc,'toloc':toloc})


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
                message="Данные благополучно добавились"
            except ObjectDoesNotExist:
                message="Введенные геоданные нет в базе"
                return render(request,"addfreight.html",{"addfr":addfr,"message": message})

        else:
            message="Попробуйте заново"

    return render(request, "addfreight.html",{"addfr":addfr,"message":message,"fromloc":fromloc,"toloc":toloc,"weight":weight,"comment":comment,"contact":contact, 'fromid':fromLocation})