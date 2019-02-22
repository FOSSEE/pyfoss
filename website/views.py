from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from website.models import FOSSEEStats, TBCPYTHONBook

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
    context = {}

    if permalink == 'python-workshops':
        blocks = get_blocks()
        rows = FOSSEEStats.objects.using('fossee_new').filter(foss_name='Python', type ='Workshop').order_by('-w_id')
        print("----------", rows)
        python_wokshop_page_content = Page.objects.get(permalink='python-workshops-page')
        context = {
            'page':python_wokshop_page_content,
            'navs': blocks['navs'],
            'sidebar': blocks['sidebar'],
            'footer': blocks['footer'],
            'permalink': permalink,
            'obj': rows
        }

    if permalink == 'textbook-companions-for-academics':
        blocks = get_blocks()
        textbook_companions_for_academics = Page.objects.get(permalink='textbook-companions-for-academics-page')
        completed_books = TBCPYTHONBook.objects.using('tbcpython').values('id', 'title', 'author').filter(approved=True).order_by('id')

        context = {
            'page':textbook_companions_for_academics,
            'navs': blocks['navs'],
            'sidebar': blocks['sidebar'],
            'footer': blocks['footer'],
            'permalink': permalink,
            'obj': completed_books
        }

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
        context['permalink'] = permalink

    if permalink != 'home' and permalink != 'python-workshops' and permalink != 'textbook-companions-for-academics':
        page = get_object_or_404(Page, permalink=permalink)
        blocks = get_blocks()
        context = {
            'page': page,
            'navs': blocks['navs'],
            'sidebar': blocks['sidebar'],
            'footer': blocks['footer'],
            'permalink': permalink
        }
    return render(request, "website/page.html", context)

