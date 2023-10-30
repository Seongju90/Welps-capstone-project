from flask import Blueprint, jsonify, request
from app.models import Restaurant, Review, RestaurantImage, Category, User,db
from .auth_routes import validation_errors_to_error_messages
from thefuzz import fuzz
from thefuzz import process
from .restaurants_routes import round_to_nearest_half

# fuzz uses Levenshtein distance string metric for measuring strings.

search_routes = Blueprint('search', __name__)


@search_routes.route("")
def search_restaurants():
    # Get query from request
    query = request.args.get('query')
    print('queryeryeyreyrye', query)

    # Query for all the restaurants then convert it to dictionary
    restaurants = Restaurant.query.all()
    restaurants_dict = [restaurant.to_dict() for restaurant in restaurants]

    # Extract name only and make a list to use for fuzz search
    restaurant_names = [res['name'] for res in restaurants_dict]

    # Peform fuzz search comparing search query to the restaurant names
    # Search data structure [('Chungdam', 77), ('Lock Chun', 57)] List of tuples, number = score
    # token sort ratio calculates simliarity between strings irrelvant of order, matches each word and looks at overall content as whole.
    search_results = process.extract(query, restaurant_names, scorer=fuzz.token_sort_ratio, limit=5)

    # Threshold score=40 seems to be where results are randomized and not pertaining to the search keyword at all
    # Set results found variable to default true, if all of the search results are under 40 set variable to false
    results_found = False

    # Loop through the result scores to see if their threshold is above 40
    for results in search_results:
        score = results[1]
        if score > 40:
            results_found = True

    # Loop through the search result and query for the restaurant data using the name and append to new list
    search_restaurant_list = []
    for result in search_results:
        # Because search data is list of tuples, the index[0] is the name
        search_restaurants = Restaurant.query.filter(Restaurant.name.ilike(f"%{result[0]}%")).one()
        search_restaurant_list.append(search_restaurants)

    # Turn resulted search list into dictionaries
    search_restaurants_dict = [search_rest.to_dict() for search_rest in search_restaurant_list]

    # Add all information needed, reviews, images, categories
    for search_restaurant in search_restaurants_dict:

        reviews = Review.query.filter(Review.restaurant_id == search_restaurant['id']).all()
        images = RestaurantImage.query.filter(RestaurantImage.restaurant_id == search_restaurant['id']).all()
        categories = Category.query \
                    .join(Category.restaurant) \
                    .filter(Restaurant.id == search_restaurant['id']) \
                    .all()

        # Turn all the return from queries into dict so I can manipulate the data
        review_dict = [ review.to_dict() for review in reviews]
        images_dict = [ image.to_dict() for image in images]
        categories_dict = [ category.to_dict() for category in categories]

        # if there are no reviews avgRating is 0, otherwise calculate avgRating
        if (len(review_dict) == 0):
            avgRating = 0
        else:
        # Calculate avgRating and add it to the review dict
            totalRatings = 0
            for review in review_dict:
                totalRatings += review['rating']
            # calculate the avg, use round to get 1 decimal place, then round again to nearest half
            avgRating = round(totalRatings / len(review_dict), 1)
            avgRating = round_to_nearest_half(avgRating)

        # Add information to each restaurant
        search_restaurant["avgRating"] = avgRating
        search_restaurant['reviews'] = review_dict
        search_restaurant['images'] = images_dict
        search_restaurant['categories'] = categories_dict

    return {"Search": search_restaurants_dict, "Results": results_found}
