from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, db, Restaurant, User, ReviewImage
from app.forms import ReviewForm
from .auth_routes import validation_errors_to_error_messages
import random

reviews_routes = Blueprint('reviews', __name__)


# Edit a review based on it's id
@reviews_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_review(id):
    """
    Edit a review based on it's id
    """
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    review_to_edit = Review.query.get(id)

    if form.validate_on_submit():
        review_to_edit.review=form.data["review"]
        review_to_edit.rating=form.data["rating"]

        db.session.commit()
        return review_to_edit.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# Delete a review based on it's id
@reviews_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_review(id):
    """
    Delete a review based on it's id
    """

    review_to_delete = Review.query.get(id)

    if (review_to_delete.user_id == current_user.id):
        db.session.delete(review_to_delete)
        db.session.commit()

        return jsonify({
            "message": "Successfully deleted the restaurant"
        })

    else:
        return jsonify({
            "message": "Forbidden, you are not the owner of the review",
            "status_code": 403
        }), 403


@reviews_routes.route('')
def splash_page_reviews():
    """
    Loading all the reviews and selecting 6 to load on the splash page
    """

    # Later Add Distinct query

    splash_reviews = Review.query.all()
    splash_reviews_dict = [reviews.to_dict() for reviews in splash_reviews]

    # Shuffle the order of restaurant, then select only 6 to view on splash
    random.shuffle(splash_reviews_dict)
    shuffled_reviews_dict = splash_reviews_dict[:6]

    # For each review, attach user info, review images, restaurant info
    for review in shuffled_reviews_dict:

        restaurant = Restaurant.query.get(review["restaurant_id"])
        user_info = User.query.filter(User.id == review['user_id']).one()
        review_images = ReviewImage.query.filter(ReviewImage.review_id == review['id']).all()

        restaurant_dict = restaurant.to_dict()
        user_info_dict = user_info.to_dict()
        review_images_dict = [image.to_dict() for image in review_images]

        review["restaurant_info"] = restaurant_dict
        review["user_info"] = user_info_dict
        review["review_images"] = review_images_dict

    return {"Splash_Reviews": shuffled_reviews_dict}
