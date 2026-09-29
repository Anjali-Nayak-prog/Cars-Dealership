from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('djangoapp/', include('djangoapp.urls')),

    path(
        '',
        TemplateView.as_view(template_name='Home.html'),
        name='home'
    ),

    path(
        'login',
        TemplateView.as_view(template_name='Login.html'),
        name='login_page'
    ),

    path(
        'dealers',
        views.dealers_page,
        name='dealers'
    ),

    path(
        'about',
        TemplateView.as_view(template_name='About.html'),
        name='about'
    ),

    path(
        'contact',
        TemplateView.as_view(template_name='Contact.html'),
        name='contact'
    ),

    path(
        'analyze/<str:review_text>',
        views.analyze_review_get,
        name='analyze_review_get'
    ),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)