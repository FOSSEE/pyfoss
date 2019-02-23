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
    sidebar = Block.objects.get(block_name="sidebar")
    footer = Block.objects.get(block_name="footer")
    blocks = {
        'navs': Nav.objects.order_by('position'),
        'sidebar': block_sort(sidebar),
        'footer': block_sort(footer)
    }
    return blocks


def dispatcher(request, permalink=''):

    blocks = get_blocks()
    context = {
        'navs': blocks['navs'],
        'sidebar': blocks['sidebar'],
        'footer': blocks['footer'],
        'permalink': permalink,
    }

    if permalink == 'python-workshops':
        rows = FOSSEEStats.objects.using('fossee_new').filter(
            foss_name='Python', type='Workshop').order_by('-w_id')
        python_wokshop_page_content = Page.objects.get(
            permalink='python-workshops-page')
        context['page'] = python_wokshop_page_content
        context['obj'] = rows

    if permalink == 'textbook-companions-for-academics':
        textbook_companions_for_academics = Page.objects.get(
            permalink='textbook-companions-for-academics')
        completed_books = TBCPYTHONBook.objects.using('tbcpython').values(
            'id', 'title', 'author').filter(approved=True).order_by('id')
        context['page'] = textbook_companions_for_academics
        context['obj'] = completed_books

    if permalink == '' or permalink == 'home':
        permalink = 'home'
        page = get_object_or_404(Page, permalink=permalink)
        context['page'] = page

    if permalink != 'home' and permalink != 'python-workshops' and permalink != 'textbook-companions-for-academics':
        page = get_object_or_404(Page, permalink=permalink)
        context['page'] = page

    return render(request, "website/page.html", context)
