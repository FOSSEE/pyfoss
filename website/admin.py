
from django.contrib import admin
from nested_inline.admin import (NestedModelAdmin, NestedStackedInline,
                                 NestedTabularInline)

from website.models import (Nav, SubNav, Page, Link,
                            LinkBox, TextBox, Block, Banner)


class SubNavInline(admin.TabularInline):
    model = SubNav
    extra = 0


class NavAdmin(admin.ModelAdmin):
    list_display = ('nav_name', 'link', 'visible')
    inlines = [SubNavInline]


class PageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'permalink', 'visible')


class LinkInline(NestedTabularInline):
    model = Link
    extra = 0


class LinkBoxInline(NestedStackedInline):
    model = LinkBox
    inlines = [LinkInline]
    extra = 0


class TextBoxInline(NestedStackedInline):
    model = TextBox
    extra = 0


class BlockAdmin(NestedModelAdmin):
    model = Block
    inlines = [LinkBoxInline, TextBoxInline]


admin.site.register(Nav, NavAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Banner)
