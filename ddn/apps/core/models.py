from django.db import models
from django.urls import reverse


class Types(models.Model):
	name = models.CharField(
		verbose_name="Тип товара",
		max_length=255,
		blank=False,
		null=False)
	published = models.DateTimeField(
		auto_now_add=True,
		db_index=True,
		verbose_name='Дата публикации')
	slug = models.SlugField(
		unique=True,
		db_index=True,
		null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('core:types', kwargs={'type_slug': self.slug})

	class Meta:
		verbose_name = "Тип товара"
		verbose_name_plural = "Типы товаров"
		ordering = ['name']


class Goods(models.Model):
	name = models.CharField(
		verbose_name="Название товара",
		max_length=255,
		blank=False,
		null=False)
	description = models.TextField(
		verbose_name="Описание товара",
		blank=False,
		null=False)
	price = models.FloatField(
		verbose_name="Цена товара",
		blank=False,
		null=False)
	type_good = models.ForeignKey(
		Types,
		on_delete=models.PROTECT,
		related_name='+')
	slug = models.SlugField(
		unique=True,
		db_index=True,
		null=True,
		allow_unicode=True)
	pub_date = models.DateTimeField(
		auto_now_add=True,
		db_index=True,
		verbose_name='Дата публикации')
	pub_update = models.DateField(
		auto_now=True,
		verbose_name='Дата обновления публикации')
	published = models.BooleanField(null=True)

	def __str__(self):
		return f"{self.name} with price: {self.price} \
			type: {self.type_good}"

	def get_absolute_url(self):
		return reverse('core:goods', kwargs={'good_slug': self.slug})

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
		ordering = ['name', 'type_good']
