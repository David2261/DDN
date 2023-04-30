from django.contrib import admin

from .models import Types, Goods


class GoodsAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'pub_date', 'published')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'description', 'pub_date')
	list_editable = ('published', )
	list_filter = ('published', 'pub_date')
	prepopulated_fields = ({'slug': ("name", )})
	fields = (
		'name', 'description', 'price', 'type_good', 'slug', 'published')
	readonly_field = ('pub_date', 'pub_update', )


class TypesAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	search_fields = ('name', )
	prepopulated_fields = ({"slug": ("name", )})


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Types, TypesAdmin)

admin.site.site_title = "Админ панель сайта DDN"
admin.site.header_title = "Админ панель сайта DDN"
