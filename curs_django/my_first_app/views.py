from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def my_view(request):
    car_list = [
        {"title": "BMV"},
        {"title": "Mazda"}
    ]
    context = {
        "carlist": car_list
    }
    return render(request, 'my_first_app/car_list.html', context)

def my_test_view(request, *args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    return HttpResponse("")

class CarListView(TemplateView):
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self):
        car_list = [
        {"title": "BMV"},
        {"title": "Mazda"}
        ]
        return {
            "carlist": car_list
        }