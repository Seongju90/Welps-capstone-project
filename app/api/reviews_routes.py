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
    print('backend####################', review_to_edit)

    if form.validate_on_submit():
        review_to_edit.review=form.data["review"]
        review_to_edit.rating=form.data["rating"]

        db.session.commit()
        return review_to_edit.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
