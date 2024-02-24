from django.shortcuts import render
import json

def car_list(request):
    with open('static/car.json', 'r') as json_file:
        car_data = json.load(json_file)['cars']
    return render(request, 'cars/car_list.html', {'car_data': car_data})