from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from website.models import FOSSEEStats

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
	if permalink == 'python-workshops':
		blocks = get_blocks()
		rows = FOSSEEStats.objects.using('fossee_in').filter(foss_name='Python', type ='Workshop').order_by('-w_id')

		context = {
			'navs': blocks['navs'],
			'sidebar': blocks['sidebar'],
			'footer': blocks['footer'],
			'permalink': permalink,
			'obj' : rows,
		}
		#rows = FOSSEEStats.objects.using('fossee_in').all()
		#return render(request, 'website/templates/test.html',context)

	if permalink == '' or permalink == 'home' :
		permalink = 'home'
		page = get_object_or_404(Page, permalink=permalink)
		blocks = get_blocks()
		context = {
			'page': page,
			'navs': blocks['navs'],
			'sidebar': blocks['sidebar'],
			'footer': blocks['footer'],
			'permalink': permalink
		}

	if permalink != 'home' and permalink != 'python-workshops':
		page = get_object_or_404(Page, permalink=permalink)
		blocks = get_blocks()
		context = {
			'page': page,
			'navs': blocks['navs'],
			'sidebar': blocks['sidebar'],
			'footer': blocks['footer'],
			'permalink': permalink
		}
	return render(request, 'website/templates/page.html', context)
