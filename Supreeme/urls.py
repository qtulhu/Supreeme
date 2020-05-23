from django.contrib import admin
from django.urls import path
from django.urls import include

from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('infirmary/', include('infirmary.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path('',RedirectView.as_view(url='/infirmary/', permanent=True)),
]
