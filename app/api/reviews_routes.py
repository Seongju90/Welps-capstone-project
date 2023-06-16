from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, db
from app.forms import ReviewForm
from .auth_routes import validation_errors_to_error_messages


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
