from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Restaurant, Review

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/restaurants')
@login_required
def my_restaurants(id):
    """
    Query for a user's restaurants by id and return it in a dictionary
    """
    restaurants = Restaurant.query.filter(Restaurant.owner_id == id)

    return {"Restaurants": restaurants.to_dict()}


@user_routes.route('/<int:id>/reviews')
@login_required
def my_reviews(id):
    """
    Query for user's reviews by id and return it in a dictionary
    """
    reviews = Review.query.filter(Review.user_id == id)

    return {"Reviews": reviews.to_dict()}
