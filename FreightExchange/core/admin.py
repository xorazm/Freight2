from django.contrib import admin

# Register your models here.
from .models import *
from django import forms



class GeoLocationsAdmin(admin.ModelAdmin):
    list_display = ('id','GeoLocationName','GeoLocationParentId','GeoLocationTypeId')
    search_fields = ('GeoLocationName','GeoLocationParentId__GeoLocationName','GeoLocationTypeId__GeoLocationType')


class FreightsModelForm( forms.ModelForm ):
    Comment = forms.CharField( widget=forms.Textarea ,label="Инфо")
    class Meta:
        model = Freights
        fields = '__all__'

class FreightsAdmin(admin.ModelAdmin):
    form = FreightsModelForm


admin.site.register(GeoLocations,GeoLocationsAdmin)
admin.site.register(GeoLocationType)
admin.site.register(Freights,FreightsAdmin)



