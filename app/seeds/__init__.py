from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .restaurant_categories import seed_restaurant_categories, undo_restaurant_categories
from .favorites import seed_favorites, undo_favorites
from .restaurant_images import seed_restaurant_images, undo_restaurant_images
from .restaurants import seed_restaurants, undo_restaurants
from .review_images import seed_review_images, undo_review_images
from .reviews import seed_reviews, undo_reviews

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_favorites()
        undo_restaurant_categories()
        undo_review_images()
        undo_restaurant_images()
        undo_categories()
        undo_reviews()
        undo_restaurants()
        undo_users()
    # Add other seed functions here
    seed_users()
    seed_restaurants()
    seed_reviews()
    seed_categories()
    seed_restaurant_images()
    seed_review_images()
    seed_restaurant_categories()
    seed_favorites()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    # Add other undo functions here
        undo_favorites()
        undo_restaurant_categories()
        undo_review_images()
        undo_restaurant_images()
        undo_categories()
        undo_reviews()
        undo_restaurants()
        undo_users()
