from flask import Blueprint, jsonify, request
from app.models import Restaurant, db
from .auth_routes import validation_errors_to_error_messages


search_routes = Blueprint('search', __name__)


@search_routes.route("")
def search_restaurants():
    # Get query from request
    query = request.args.get('query')
    results = Restaurant.query.filter(Restaurant.name.ilike(f'%{query}')).all()
    return;
