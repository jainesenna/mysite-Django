from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Bom dia, que tal ouvir Vor Í Vaglaskógi de Kaleo")