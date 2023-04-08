from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GeoLocations(models.Model):
    GeoLocationName=models.CharField(max_length=50,verbose_name='Название')
    GeoLocationParentId=models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=models.CASCADE,verbose_name='Родитель')
    GeoLocationTypeId=models.ForeignKey('GeoLocationType',on_delete=models.CASCADE, verbose_name='Тип геолокации')

    def __str__(self):
        return self.GeoLocationName

    class Meta:
        verbose_name='Геолокация'
        verbose_name_plural='Геолокации'



class GeoLocationType(models.Model):
    GeoLocationType=models.CharField(max_length=10)

    def __str__(self):
        return self.GeoLocationType
    class Meta:
        verbose_name='Тип геолокации'
        verbose_name_plural='Типы геолокаций'


class Freights(models.Model):
    FromLoc=models.ForeignKey('GeoLocations',related_name='fromloc',on_delete=models.CASCADE,verbose_name='Откуда')
    ToLoc=models.ForeignKey('GeoLocations',related_name='toloc', on_delete=models.CASCADE,verbose_name='Куда')
    Weight=models.CharField(max_length=50,verbose_name='Вес')
    Comment=models.CharField(max_length=500,verbose_name='Инфо')
    SubmitedDate=models.DateField(verbose_name='Дата публикации')
    Contact=models.CharField(max_length=100,verbose_name='Контакты')
    User=models.ForeignKey(User, null=True ,on_delete=models.CASCADE, verbose_name='Пользователь')
    TLLinkMessage=models.CharField(max_length=100,null=True,verbose_name='Ссылка на пост')
    TLLinkUser = models.CharField(max_length=100, null=True, verbose_name='Ссылка на пользователя')
    Active=models.BooleanField(default=True,verbose_name='Есть на сайте')

    class Meta:
        verbose_name = 'Грузоперевозка'
        verbose_name_plural = 'Грузоперевозки'
