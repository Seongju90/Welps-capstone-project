from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Restaurant, Review, RestaurantImage, Category, db
from app.forms import RestaurantForm, EditRestaurantForm
from .auth_routes import validation_errors_to_error_messages



restaurant_routes = Blueprint('restaurants', __name__)


# In Python, you can use dot notation to access attributes of an object or properties of a class,
# but you need to use bracket notation to access elements in a dictionary or a list.


# GET for all restaurants
@restaurant_routes.route('')
def all_restaurants():
    # Query for all restaurants, then change <Python> into readable dictionary
    all_restaurants = Restaurant.query.all()
    restaurant_dict = [restaurant.to_dict() for restaurant in all_restaurants]

    # Loop through each restaurant, then find each restaurants reviews, images, categories
    for restaurant in restaurant_dict:

        reviews = Review.query.filter(Review.restaurant_id == restaurant['id']).all()
        images = RestaurantImage.query.filter(RestaurantImage.restaurant_id == restaurant['id']).all()
        # Category.restaurant =>  restaurant refers to variable defined in relationship on Category table
        categories = Category.query \
                    .join(Category.restaurant) \
                    .filter(Restaurant.id == restaurant['id']) \
                    .all()

        # Turn all the return from queries into dict so I can manipulate the data
        review_dict = [ review.to_dict() for review in reviews]
        images_dict = [ image.to_dict() for image in images]
        categories_dict = [ category.to_dict() for category in categories]

        # Add information to each restaurant
        restaurant['reviews'] = review_dict
        restaurant['images'] = images_dict
        restaurant['categories'] = categories_dict


    # Use jsonify to return Content-Type header as application/json, other it will default to text/html
    return  jsonify({"Restaurants": restaurant_dict})


# GET one restaurant
@restaurant_routes.route('/<int:id>')
def get_one_restaurant(id):

    # Take the restaurant id from the id inputted in the thunk, and reassign to variable
    restaurant_id = id

    # Query for that restaurant
    restaurant = Restaurant.query.get(id)
    restaurant_dict = restaurant.to_dict()

    # Query for the Reviews, Images, and Categories and append it to the main restaurant query after turning it into dictionary
    reviews = Review.query.filter(Review.restaurant_id == restaurant_id).all()
    images = RestaurantImage.query.filter(RestaurantImage.restaurant_id == restaurant_id).all()
    categories = Category.query \
                .join(Category.restaurant) \
                .filter(Restaurant.id == restaurant_id) \
                .all()

    # Turn all the return from queries into dict so I can manipulate the data
    review_dict = [ review.to_dict() for review in reviews]
    images_dict = [ image.to_dict() for image in images]
    categories_dict = [ category.to_dict() for category in categories]

     # Add information to each restaurant
    restaurant_dict['reviews'] = review_dict
    restaurant_dict['images'] = images_dict
    restaurant_dict['categories'] = categories_dict

    # what you return as the key Single_Restaurant here, reflects in action.payload in frontend store
    return jsonify({"Single_Restaurant": restaurant_dict})

# CREATE a restaurant
@restaurant_routes.route('', methods=['POST'])
@login_required
def create_restaurant():
    form = RestaurantForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        newRestaurant = Restaurant(
            name=form.data["name"],
            owner_id=current_user.id,
            address=form.data["address"],
            city=form.data["city"],
            state=form.data["state"],
            country=form.data["country"],
            zipcode=form.data["zipcode"],
            price=form.data["price"],
            phone_number=form.data["phone_number"],
            preview_image=form.data["preview_image"],
            start_hours=form.data["start_hours"],
            end_hours=form.data["end_hours"]
        )

        db.session.add(newRestaurant)
        db.session.commit()

        return newRestaurant.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# Edit Restaurant
@restaurant_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_my_restaurant(id):
    """
    Edit existing restaurant
    """
    form = EditRestaurantForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    restaurant_to_edit = Restaurant.query.get(id)

    print('backend route', restaurant_to_edit)
    if form.validate_on_submit():

        # no commas at the end or it will turn everything into tuples
        restaurant_to_edit.name=form.data["name"]
        restaurant_to_edit.owner_id=current_user.id
        restaurant_to_edit.address=form.data["address"]
        restaurant_to_edit.city=form.data["city"]
        restaurant_to_edit.state=form.data["state"]
        restaurant_to_edit.country=form.data["country"]
        restaurant_to_edit.zipcode=form.data["zipcode"]
        restaurant_to_edit.price=form.data["price"]
        restaurant_to_edit.phone_number=form.data["phone_number"]
        restaurant_to_edit.preview_image=form.data["preview_image"]
        restaurant_to_edit.start_hours=form.data["start_hours"]
        restaurant_to_edit.end_hours=form.data["end_hours"]

        db.session.commit()
        return restaurant_to_edit.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# Delete a Restaurant
@restaurant_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_my_restaurant(id):
    """
    Delete a restaurant
    """

    restaurant_to_delete = Restaurant.query.get(id)
    print('backend, again', restaurant_to_delete)
    print('backend', restaurant_to_delete.owner_id)

    if (restaurant_to_delete.owner_id == current_user.id):
        db.session.delete(restaurant_to_delete)
        db.session.commit()

        return jsonify({
            "message": "Successfully deleted the restaurant"
        })

    else:
        return jsonify({
            "message": "Forbidden, you are not the owner of the review",
            "status_code": 403
        }), 403
