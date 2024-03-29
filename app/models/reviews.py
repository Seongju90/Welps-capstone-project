from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Review(db.Model):
    __tablename__ = "reviews"


    if environment == "production":
        __table_args__  = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('restaurants.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    review = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # timezone=True, boolean indicates that the datetime type should enable timezone support
    # server_default, the default value is generated by the database server, while default is specified yourself in the model
    # onupdate, built in update function,
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=datetime.now)


    user = db.relationship('User', back_populates='review')
    image = db.relationship('ReviewImage', back_populates='review', cascade="all, delete")
    restaurant = db.relationship('Restaurant', back_populates='review')

    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'user_id': self.user_id,
            'review': self.review,
            'rating': self.rating,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
