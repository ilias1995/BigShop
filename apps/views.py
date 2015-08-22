from django.shortcuts import render, get_object_or_404
from apps.models import Cars, Form_car, Type_for_car


def index(request):
    return render(request, 'index.html')


def cars(request):
    spare_parts = Type_for_car.objects.all()
    cars = Cars.objects.all()
    return render(request, 'cars.html', {'cars': cars, 'spare_parts': spare_parts})

def info_car(request, id):
    cars = Cars.objects.get(pk=id)
    return render(request, 'info_car.html', {'cars': cars})

def spare_parts(request, type_for_car_id):
    spare_parts = Type_for_car.objects.all()
    for_car = Type_for_car.objects.all().order_by('-name')
    type_for_car = get_object_or_404(Type_for_car, pk=type_for_car_id )
    return render(request, 'spare_parts.html', {'type_for_car': type_for_car, 'for_car': for_car, 'spare_parts': spare_parts})


def info_spare_parts(request, id):
    info_form_cars = Form_car.objects.get(pk=id)
    return render(request, 'info_spare_parts.html', {'info_form_cars': info_form_cars})