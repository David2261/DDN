from django.db.models import Count

from .models import Types


class DataMixin:
	paginate_by = 5

	def get_user_context(self, **kwargs):
		context = kwargs
		types = Types.objects.annotate(Count('name'))
		context['types'] = types
		context['type_selected'] = 0
		return context
