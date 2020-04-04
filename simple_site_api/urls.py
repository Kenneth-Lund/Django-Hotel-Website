from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('latest/page=<int:page_number>/', views.PublicLatest.as_view()),
    path('room/id=<int:ID>/', views.PublicRoom.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)