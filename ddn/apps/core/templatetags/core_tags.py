from django import template

from core.models import Types

register = template.Library()


@register.simple_tag(name='gettypes')
def get_types(filter=None):
	if not filter:
		context = Types.objects.all()
	else:
		context = Types.objects.filter(pk=filter)
	return context


@register.inclusion_tag('core/list_types.html')
def show_types(sort=None, type_selected=0):
	if not sort:
		types = Types.objects.all()
	else:
		types = Types.objects.order_by(sort)
	return {"types": types, "type_selected": type_selected}
