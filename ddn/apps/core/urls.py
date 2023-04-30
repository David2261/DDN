from django.urls import path
from .views import HomePage, TypesPage, GoodsPage


app_name = 'core'
urlpatterns = [
	path('', HomePage.as_view(), name="home"),
	path('types/<slug:type_slug>/', TypesPage.as_view(), name="types"),
	path(
		'goods/<slug:good_slug>/',
		GoodsPage.as_view(),
		name="goods"),
]
