from django.urls import path
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),

    path(
        'get_dealer_reviews/<int:dealer_id>',
        views.get_dealer_reviews,
        name='get_dealer_reviews'
    ),

    path(
        'get_dealerships',
        views.get_dealerships,
        name='get_dealerships'
    ),

    path(
        'get_dealer_details/<int:dealer_id>',
        views.get_dealer_details,
        name='get_dealer_details'
    ),

    path(
        'get_dealers_by_state/<str:state>',
        views.get_dealers_by_state,
        name='get_dealers_by_state'
    ),

    path(
        'get_cars',
        views.get_cars,
        name='getcars'
    ),

    path(
        'analyze_review',
        views.analyze_review,
        name='analyze_review'
    ),

    path(
        'dealer/<int:dealer_id>',
        views.dealer_page,
        name='dealer_page'
    ),

    path(
        'post_review',
        views.post_review_page,
        name='post_review'
    ),

    path(
        'add_review',
        views.add_review,
        name='add_review'
    ),
]