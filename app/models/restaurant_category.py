from .db import db, environment, SCHEMA, add_prefix_for_prod


restaurant_categories = db.Table(
    'restaurant_categories',
    db.Model.metadata,
    db.Column('restaurants', db.Integer, db.ForeignKey(add_prefix_for_prod('restaurants.id')), primary_key=True),
    db.Column('categories', db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')), primary_key=True)
)

if environment == "production":
    restaurant_categories.schema = SCHEMA
