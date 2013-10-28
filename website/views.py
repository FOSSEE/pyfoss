from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from website.models import Nav, Page, Block

def block_sort(obj):
	linkboxes = obj.linkbox_set.all()
	textboxes = obj.textbox_set.all()

	items = []
	for item in linkboxes:
		items.append(item)

	for item in textboxes:
		items.append(item)

	def get_pos(x): return x.position
	items = sorted(items, key=get_pos)
	return items

def home(request):
	return render_to_response('home.html')

def dispatcher(request, permalink=''):
	page = get_object_or_404(Page, permalink=permalink)
	navs = Nav.objects.order_by('position')

	sidebar = Block.objects.get(block_name = "sidebar")
	footer = Block.objects.get(block_name = "sidebar")
	
	#
	sidebar = block_sort(sidebar)
	footer = block_sort(footer)

	context = {
		'navs': navs,
		'page': page,
		'sidebar': sidebar,
		'footer': footer
	}
	return render_to_response('page.html', context)