"""
URL configuration for djangoproj project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Django administration
    path('admin/', admin.site.urls),

    # Django application APIs and views
    path('djangoapp/', include('djangoapp.urls')),

    # Home page
    path(
        '',
        TemplateView.as_view(template_name='Home.html'),
        name='home'
    ),

    # About Us page
    path(
        'about',
        TemplateView.as_view(template_name='About.html'),
        name='about'
    ),

    # Contact Us page
    path(
        'contact',
        TemplateView.as_view(template_name='Contact.html'),
        name='contact'
    ),
]

# Serve static files during development
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)