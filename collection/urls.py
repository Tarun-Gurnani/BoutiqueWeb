from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.views.generic.base import TemplateView


app_name = 'collection'


urlpatterns = [

    # /category/
    path('', views.IndexView.as_view(), name='index'),
    # /category/<category_id>/
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    path('/', views.feedback_form, name='feedback_form'),






]