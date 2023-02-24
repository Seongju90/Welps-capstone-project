from .db import db, environment, SCHEMA, add_prefix_for_prod


class RestaurantImage(db.Model):
    __tablename__ = "restaurant_images"


    if environment == "production":
        __table_args__  = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable=False)
    url = db.Column(db.String(255), nullable=True)
    preview = db.Column(db.Boolean, default=False)


    restaurant = db.relationship('Restaurant', back_populates="image")


    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'url': self.url,
            'preview': self.preview,
        }
