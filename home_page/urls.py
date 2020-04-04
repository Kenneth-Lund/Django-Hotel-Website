from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('update-preview-list/id=<int:ID>/', views.update_preview_list, name='preview_list'),
]