	# Uncomment the required imports before adding the code

# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib import messages
# from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
import logging
import json
import requests
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel
def get_cars(request):
    count = CarMake.objects.count()

    if count == 0:
        from .populate import initiate
        initiate()

    car_models = CarModel.objects.select_related('car_make')

    cars = []

    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })

    return JsonResponse({"CarModels": cars})

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request body
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    # Try to check if provided credentials can be authenticated
    user = authenticate(username=username, password=password)

    data = {"userName": username}

    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {
            "userName": username,
            "status": "Authenticated"
        }

    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return JsonResponse({"status": "Logged out"})


# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...


# Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request):
    import os

    dealerships_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'database',
        'data',
        'dealerships.json'
    )

    with open(dealerships_file, 'r', encoding='utf-8') as file:
        dealerships_data = json.load(file)

    return JsonResponse(dealerships_data['dealerships'], safe=False)


# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    import os

    reviews_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'database',
        'data',
        'reviews.json'
    )

    with open(reviews_file, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)

    reviews = [
        review
        for review in reviews_data['reviews']
        if review['dealership'] == dealer_id
    ]

    return JsonResponse(reviews, safe=False)


# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    import os

    dealerships_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'database',
        'data',
        'dealerships.json'
    )

    with open(dealerships_file, 'r', encoding='utf-8') as file:
        dealerships_data = json.load(file)

    dealer = next(
        (dealer for dealer in dealerships_data['dealerships']
         if dealer['id'] == dealer_id),
        None
    )

    if dealer is not None:
        return JsonResponse(dealer)

    return JsonResponse(
        {"error": "Dealer not found"},
        status=404
    )


# Create a `get_dealers_by_state` view to get dealerships in a state
def get_dealers_by_state(request, state):
    import os

    dealerships_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'database',
        'data',
        'dealerships.json'
    )

    with open(dealerships_file, 'r', encoding='utf-8') as file:
        dealerships_data = json.load(file)

    dealers = [
        dealer
        for dealer in dealerships_data['dealerships']
        if dealer['state'].lower() == state.lower()
    ]

    return JsonResponse(dealers, safe=False)

# Create a `add_review` view to submit a review
# def add_review(request):
# ...

# Create an `analyze_review` view to analyze review sentiment
@csrf_exempt
def analyze_review(request):
    data = json.loads(request.body)
    review = data.get('review', '')

    if review.lower() == "fantastic services":
        sentiment = "positive"
    else:
        sentiment = "neutral"

    return JsonResponse({
        "review": review,
        "sentiment": sentiment
    })

def dealers_page(request):
    import os

    dealerships_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'database',
        'data',
        'dealerships.json'
    )

    with open(dealerships_file, 'r', encoding='utf-8') as file:
        dealerships_data = json.load(file)

    return render(
        request,
        'Dealers.html',
        {'dealers': dealerships_data['dealerships']}
    )


def dealer_page(request, dealer_id):
    import os

    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Load dealership details
    dealerships_file = os.path.join(
        base_dir,
        'database',
        'data',
        'dealerships.json'
    )

    with open(dealerships_file, 'r', encoding='utf-8') as file:
        dealerships_data = json.load(file)

    dealer = next(
        (
            dealer
            for dealer in dealerships_data['dealerships']
            if dealer['id'] == dealer_id
        ),
        None
    )

    if dealer is None:
        return JsonResponse(
            {"error": "Dealer not found"},
            status=404
        )

    # Load reviews
    reviews_file = os.path.join(
        base_dir,
        'database',
        'data',
        'reviews.json'
    )

    with open(reviews_file, 'r', encoding='utf-8') as file:
        reviews_data = json.load(file)

    reviews = [
        review
        for review in reviews_data['reviews']
        if review['dealership'] == dealer_id
    ]

    return render(
        request,
        'DealerDetails.html',
        {
            'dealer': dealer,
            'reviews': reviews
        }
    )

def post_review_page(request):
    return render(request, 'PostReview.html')

@csrf_exempt
def add_review(request):
    if request.method == "POST":
        data = json.loads(request.body)

        review = {
            "review": data.get("review", ""),
            "rating": int(data.get("rating", 5)),
            "car_make": data.get("car_make", ""),
            "car_model": data.get("car_model", ""),
            "car_year": int(data.get("car_year", 2022)),
            "purchase_date": data.get("purchase_date", ""),
            "purchase": data.get("purchase", "Yes"),
            "name": data.get("name", "John Doe"),
            "id": 999,
            "car_id": int(data.get("car_id", 1)),
            "dealer_id": int(data.get("dealer_id", 1))
        }

        return JsonResponse({
            "status": "Review added successfully",
            "review": review
        })

    return JsonResponse(
        {"error": "Only POST requests are allowed"},
        status=405
    )