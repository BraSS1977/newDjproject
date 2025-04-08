from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('Thirdpage', views.Thirdpage, name='page3'),
    path('fourthpage', views.fourthpage, name='page4'),

# Upper menu
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),
    path('terms', views.terms, name='terms'),
  ]