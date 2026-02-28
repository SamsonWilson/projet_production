"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from .view import about, ContactFormView as contact, contactbase, index, portfolio, service

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', index.as_view(), name='dashboard'),
    path('services/', service.as_view(), name='services'),
    path('about/', about.as_view(), name='about'),
    path('portfolio/', portfolio.as_view(), name='portfolio'),
    path('contact/', contact.as_view(), name='contact'),
    path('contactebase/', contactbase.as_view(), name='contactbase'),

    # path(' ', include('allauth.urls')),
    path('', include('produition.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('dashboard/', index.as_view(), name='dashboard'),
    path('services/', service.as_view(), name='services'),
    path('about/', about.as_view(), name='about'),
    path('portfolio/', portfolio.as_view(), name='portfolio'),
    path('contact/', contact.as_view(), name='contact'),
    path('contactebase/', contactbase.as_view(), name='contactbase'),
    # path(' ', include('allauth.urls')),
    path('', include('produition.urls')), 
    )