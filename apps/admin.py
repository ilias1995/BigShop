from django.contrib import admin
from .models import Cars, CarsType, Clothes, ClothesType, Electronic, ElectronicType, ForHome, ForHomeType, Type_for_car, Form_car
# Register your models here.

admin.site.register(Cars)
admin.site.register(CarsType)
admin.site.register(Clothes)
admin.site.register(ClothesType)
admin.site.register(Electronic)
admin.site.register(ElectronicType)
admin.site.register(ForHome)
admin.site.register(ForHomeType)
admin.site.register(Type_for_car)
admin.site.register(Form_car)
