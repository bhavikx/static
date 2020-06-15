from django.shortcuts import render
from django.http import HttpResponse

from .models import Images

from django.template import RequestContext

def homeView(request):
	pic = Images.objects.all()[:6]
	context = {
		'home' : 'active',
		'pic' : pic
	}
	return render(request, "dashboard.html",context)

def sofaView(request):
	pic = Images.objects.all()
	context = {
		'products' : 'active',
		'sofa' : 'active',
		'pic' : pic
	}
	return render(request, "product_sofa.html", context)

def curtainView(request):
	pic = Images.objects.all()
	context = {
		'products' : 'active',
		'curtain' : 'active',
		'pic' : pic
	}
	return render(request, "product_curtain.html", context)

def aboutUsView(request):
	context = {
		'about' : 'active'
	}
	return render(request, "about_us.html", context)

def contactUsView(request):
	context = {
		'contact' : 'active'
	}
	return render(request, "contact_us.html", context)