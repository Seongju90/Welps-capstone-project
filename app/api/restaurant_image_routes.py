from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import RestaurantImage, db, Restaurant
from .auth_routes import validation_errors_to_error_messages
from ..api.aws_helpers import get_unique_filename, remove_file_from_s3


restaurant_image_routes = Blueprint('restaurants-images', __name__)


@restaurant_image_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_images(id):
    """
    Delete image from restaurant
    """

    image_to_delete = RestaurantImage.query.get(id)
