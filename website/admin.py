from django.contrib import admin

from website.models import Nav, SubNav, Page

class SubNavInline(admin.TabularInline):
	model = SubNav
	extra = 0

class NavAdmin(admin.ModelAdmin):
	list_display = ('nav_name', 'link', 'visible')
	inlines = [SubNavInline]

class PageAdmin(admin.ModelAdmin):
	list_display = ('heading', 'permalink', 'visible')

admin.site.register(Nav, NavAdmin)
admin.site.register(Page, PageAdmin)