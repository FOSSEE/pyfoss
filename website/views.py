from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from website.models import Nav, SubNav, Page

def generate_nav():
	x=10

def home(request):
	return render_to_response('home.html')

def dispatcher(request, permalink=''):
	page = get_object_or_404(Page, permalink=permalink)
	navs = Nav.objects.all()

	context = {
		"navs": navs,
		"page": page
	}
	return render_to_response('page.html', context)