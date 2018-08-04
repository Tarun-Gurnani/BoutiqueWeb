from django.contrib import admin
from django.urls import path
from posts import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create),
    path('<id>/', views.post_detail, name='detail'),
    path('<id>/edit/', views.post_update, name='update'),
    path('<id>/delete/', views.post_delete),
]
