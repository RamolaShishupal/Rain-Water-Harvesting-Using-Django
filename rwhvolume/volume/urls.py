from django.urls import path

from . import views
urlpattern=[
path('volume/', views.volume, name='voulme'),
path('new_search/',views.new_search,name='new_search'),
]