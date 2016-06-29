
from django.shortcuts import render
from models import Beer
from django.http import HttpResponse


def index(request):
	beers = Beer.objects().to_json()
	return HttpResponse(beers)
