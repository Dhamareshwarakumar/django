from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.id = 1
    dest1.price = 700
    dest1.name = 'Mumbai'
    dest1.desc = "The city that never sleeps"
    dest1.img = 'destination_1.jpg'

    dest2 = Destination()
    dest2.id = 2
    dest2.price = 650
    dest2.name = 'Hyderabad'
    dest2.desc = "First Birynai, then shervani"
    dest2.img = 'destination_2.jpg'

    dest3 = Destination()
    dest3.id = 3
    dest3.price = 750
    dest3.name = 'Bengaluru'
    dest3.desc = "The Tech City"
    dest3.img = 'destination_3.jpg'

    dests = [dest1, dest2, dest3]

    return render(request, 'index.html.j2', {'dests': dests})
