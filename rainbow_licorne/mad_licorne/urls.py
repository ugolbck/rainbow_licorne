from django.urls import path
from mad_licorne import views

app_name = 'mad_licorne'
urlpatterns = [
    path('', views.index, name='index'),
	path('article/<slug:slug>', views.article, name='article'),
]