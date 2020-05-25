from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.id = 1
    dest1.price = 700
    dest1.name = 'Mumbai'
    dest1.desc = "The city that never sleeps"

    return render(request, 'index.html', {'dest1': dest1})
