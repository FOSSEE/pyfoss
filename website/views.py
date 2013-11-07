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

def get_blocks():
    sidebar = Block.objects.get(block_name = "sidebar")
    footer = Block.objects.get(block_name = "footer")
    blocks = {
        'navs': Nav.objects.order_by('position'),
        'sidebar': block_sort(sidebar),
        'footer': block_sort(footer)
    }
    return blocks

def dispatcher(request, permalink=''):
    if permalink == '':
        permalink = 'home'

    page = get_object_or_404(Page, permalink=permalink)
    blocks = get_blocks()
    context = {
		'page': page,
		'navs': blocks['navs'],
		'sidebar': blocks['sidebar'],
		'footer': blocks['footer']
	}
    return render_to_response('page.html', context)
