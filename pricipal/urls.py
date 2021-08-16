from django.urls import path
from pricipal.views import index_view


urlpatterns = [
	path('', index_view, name='index'),
]
