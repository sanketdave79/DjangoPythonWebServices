
import json
import django.core.serializers
from django.shortcuts import render
from models import Beer
from django.utils import simplejson
from django.http import HttpResponse
from bson import json_util
from pprint import pprint



def index(request):
	beers = Beer.objects().to_json()
	#customers = django.core.serializers.serialize('json',[customers,])
	
	
	return HttpResponse(beers)
	