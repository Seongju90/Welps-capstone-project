from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Restaurant, Review, RestaurantImage, Category, restaurant_categories


restaurant_routes = Blueprint('restaurants', __name__)


# GET for all restaurants
@restaurant_routes.route('/')
def all_restaurants():
    # Query for all restaurants, then change <Python> into readable dictionary
    all_restaurants = Restaurant.query.all()
    restaurant_dict = [restaurant.to_dict() for restaurant in all_restaurants]

    # Loop through each restaurant, then find each restaurants reviews, images, categories
    for restaurant in restaurant_dict:
        reviews = Review.query.filter(Review.restaurant_id == restaurant['id']).all()
        images = RestaurantImage.query.filter(RestaurantImage.restaurant_id == restaurant['id']).all()
        # Category.restaurant =>  restaurant refers to variable defined in relationship on Category table
        categories = Category.query \
                    .join(Category.restaurant) \
                    .filter(Restaurant.id == restaurant['id']) \
                    .all()

        # Turn all the return from queries into dict so I can manipulate the data
        review_dict = [ review.to_dict() for review in reviews]
        images_dict = [ image.to_dict() for image in images]
        categories_dict = [ category.to_dict() for category in categories]

        # Add information to each restaurant
        restaurant['reviews'] = review_dict
        restaurant['images'] = images_dict
        restaurant['categories'] = categories_dict


    return  jsonify({"Restaurants": restaurant_dict})
