from flask import Blueprint
from flask_login import login_required
from app.models import Restaurant, Review, RestaurantImage, Category, restaurant_categories



restaurant_routes = Blueprint('restaurants', __name__)


# GET for all restaurants
@restaurant_routes.route('/')
def all_restaurants():
    all_restaurants = Restaurant.query.all()

    return { }
