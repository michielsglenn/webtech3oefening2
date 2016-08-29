from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import examen


def index(request):
	template = loader.get_template('examen/index.html')
	return HttpResponse(template.render(request))
# Create your views here.


def detail(request):
	latest_examen_list = examen.objects.order_by('-examen_date')
	template = loader.get_template('examen/overzicht.html')
	context ={'latest_examen_list':latest_examen_list,}
	return HttpResponse(template.render(context,request))
	


	