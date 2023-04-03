
from django import forms
from captcha.fields import CaptchaField

class AddFreight(forms.Form):
    FromLoc=forms.CharField(label="Откуда",max_length=100)
    ToLoc=forms.CharField(label="Куда",max_length=100)
    Weight=forms.CharField(label="Вес",max_length=20)
    Comment=forms.CharField(label="Информация о грузе",widget=forms.Textarea)
    Contact=forms.CharField(label="Контакты",max_length=30)
    captcha = CaptchaField()