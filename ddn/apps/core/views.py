from django.views.generic import ListView, DetailView

from .models import Types, Goods
from .mixins import DataMixin


class HomePage(DataMixin, ListView):
	model = Goods
	template_name = "core/main.html"
	context_object_name = 'goods'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		type_good = self.get_user_context()
		return dict(list(context.items()) + list(type_good.items()))

	def get_queryset(self):
		return Goods.objects.filter(published=True)\
			.select_related('type_good')


class TypesPage(DataMixin, ListView):
	model = Goods
	template_name = 'core/main.html'
	context_object_name = 'goods'
	# 404
	allow_empty = False

	def get_queryset(self):
		return Goods.objects.filter(
			type_good__slug=self.kwargs['type_slug'],
			published=True).select_related('type_good')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		t = Types.objects.get(slug=self.kwargs['type_slug'])
		t_def = self.get_user_context(type_selected=t.pk)
		return dict(list(context.items()) + list(t_def.items()))


class GoodsPage(DataMixin, DetailView):
	model = Goods
	template_name = 'core/good.html'
	slug_url_kwarg = 'good_slug'
	context_object_name = 'good'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		good_def = self.get_user_context()
		return dict(list(context.items()) + list(good_def.items()))
