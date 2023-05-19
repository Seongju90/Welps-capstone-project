from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, db
from .auth_routes import validation_errors_to_error_messages


reviews_routes = Blueprint('reviews', __name__)
