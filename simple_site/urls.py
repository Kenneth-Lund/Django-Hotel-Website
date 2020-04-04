from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home-page/', include("home_page.urls")),
    path('api/', include("simple_site_api.urls")),
    path('admin/', admin.site.urls)
]
