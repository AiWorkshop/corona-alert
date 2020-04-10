from django.shortcuts import render

from .models import *
from .filters import *


def home(request):
    context = {
    }
    return render(request, 'home.html', context)

def district(request):

    coronas =  CoronaVirus.objects.all()
    myFilter = CoronaFilter(request.GET, queryset=coronas)
    coronas = myFilter.qs
    print(myFilter.form)
    context = {
        'coronas': coronas,
        'myFilter': myFilter,
    }
    return render(request, 'district.html', context)