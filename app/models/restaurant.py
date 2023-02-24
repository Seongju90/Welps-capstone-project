from .db import db, environment, SCHEMA, add_prefix_for_prod
from .favorite import favorites
from .restaurant_category import restaurant_categories

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

# The main reason we have to set a schema on deployment to render is because we are only ever using a single database instance there.
# In order to compartmentalize the db on Render we have to associate each db with a specific schema that we setup in the .env file
# Multiple projects use the same database, and this line of code is saying which schema to use.
    if environment == "production":
        __tableargs__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    zipcode = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False, unique=True)
    preview_image = db.Column(db.String(255), nullable=True)
    start_hours = db.Column(db.String(255), nullable=False)
    end_hours = db.Column(db.String(255), nullable=False)


    owner = db.relationship('User', back_populates='restaurant')
    image = db.relationship('RestaurantImage', back_populates="restaurant", cascade="all, delete")


    restaurants = db.relationship(
        'User',
        secondary=favorites,
        back_populates="favorite"
    )

    # this property will return a list
    types = db.relationship(
        'Category',
        secondary=restaurant_categories,
        back_populates="restaurant"
    )


    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'zipcode': self.zipcode,
            'price': self.price,
            'phone_number': self.phone_number,
            'preview_image': self.preview_image,
            'start_hours': self.start_hours,
            'end_hours': self.end_hours
        }
