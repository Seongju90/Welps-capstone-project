from .db import db, environment, SCHEMA
from .restaurant_category import restaurant_categories

class Category(db.Model):
    __tablename__ = "categories"


    if environment == "production":
        __tableargs__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))


    restaurant = db.relationship(
        'Restaurant',
        secondary=restaurant_categories,
        back_populates='types'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type
        }
