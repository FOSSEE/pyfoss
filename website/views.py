from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from website.models import Nav, Page, Block, Banner, FOSSEEStats


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
        'footer': block_sort(footer),
    }
    return blocks


def dispatcher(request, permalink=''):

    blocks = get_blocks()
    banner = Banner.objects.filter(visible=1)
    context = {
        'navs': blocks['navs'],
        'sidebar': blocks['sidebar'],
        'footer': blocks['footer'],
        'permalink': permalink,
    }
    if not banner:
        context['banner'] = ''
    else:
        context['banner'] = banner[0]

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
        context['page'] = textbook_companions_for_academics

    if permalink == '' or permalink == 'home':
        permalink = 'home'
        page = get_object_or_404(Page, permalink=permalink)
        context['page'] = page

    if permalink != 'home' and permalink != 'python-workshops' and \
            permalink != 'textbook-companions-for-academics':
        page = get_object_or_404(Page, permalink=permalink)
        context['page'] = page

    return render(request, "page.html", context)
