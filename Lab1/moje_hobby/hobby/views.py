
from django.shortcuts import render

def home(request):
    context = {
        "hobby_name": "Lech Poznań",
        "description": "Moim hobby jest piłka nożna. Interesuję się rozgrywkami Ekstraklasy, analizą taktyczną oraz grami menedżerskimi."
    }

    return render(request, "hobby/home.html", context)


def about(request):
    return render(request, "hobby/about.html")


def gallery(request):
    return render(request, "hobby/gallery.html")
