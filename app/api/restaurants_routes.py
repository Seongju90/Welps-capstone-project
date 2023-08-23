from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Restaurant, Review, ReviewImage, RestaurantImage, Category, User, db
from app.forms import RestaurantForm, EditRestaurantForm, ReviewForm
from .auth_routes import validation_errors_to_error_messages
from ..api.aws_helpers import get_unique_filename, upload_file_to_s3, allowed_file

restaurant_routes = Blueprint('restaurants', __name__)

# Helper function to round a number to nearest half
def round_to_nearest_half(number):
    # multiple the avgRating by 2, to turn decimal into integer, then use round() to turn into whole number.
    rounded_number = round(number * 2) / 2
    return rounded_number

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

        # if there are no reviews avgRating is 0, otherwise calculate avgRating
        if (len(review_dict) == 0):
            avgRating = 0
        else:
        # Calculate avgRating and add it to the review dict
            totalRatings = 0
            for review in review_dict:
                totalRatings += review['rating']
            # calculate the avg, use round to get 1 decimal place, then round again to nearest half
            avgRating = round(totalRatings / len(review_dict), 1)
            avgRating = round_to_nearest_half(avgRating)

        # Add information to each restaurant
        restaurant["avgRating"] = avgRating
        restaurant['reviews'] = review_dict
        restaurant['images'] = images_dict
        restaurant['categories'] = categories_dict


    # Use jsonify to return Content-Type header as application/json, other it will default to text/html
    return  {"Restaurants": restaurant_dict}


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

    # if there are no reviews avgRating is 0, otherwise calculate avgRating
    if (len(review_dict) == 0):
        avgRating = 0
    else:
        # Calculate avgRating and add it to the review dict
        totalRatings = 0
        for review in review_dict:
            totalRatings += review['rating']

        # calculate the avg, use round to get 1 decimal place, then round again to nearest half
        avgRating = round(totalRatings / len(review_dict), 1)
        avgRating = round_to_nearest_half(avgRating)

     # Add information to each restaurant
    restaurant_dict["avgRating"] = avgRating
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
        image = request.files["image"]

        if not allowed_file(image.filename):
            return {"errors": "file type not permitted"}, 400

        image.filename = get_unique_filename(image.filename)
        # if upload is successfuly will return a key "url" and the value is the url
        upload = upload_file_to_s3(image)

        if "url" not in upload:
            # if the dictionary doesn't have a url key
            # it means that there was an error when we tried to upload
            # so we send back that error message
            return upload, 400

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
            preview_image=upload["url"],
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

    categories = Category.query \
        .join(Category.restaurant) \
        .filter(Restaurant.id == restaurant_to_edit.id) \
        .all()
    categories_dict = [ category.to_dict() for category in categories]

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

        # Added this portion so that my profile page, renders the categories on update
        edit_restaurant_dict = restaurant_to_edit.to_dict()
        edit_restaurant_dict['categories'] = categories_dict

        db.session.commit()

        return edit_restaurant_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# Delete a Restaurant
@restaurant_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_my_restaurant(id):
    """
    Delete a restaurant
    """

    restaurant_to_delete = Restaurant.query.get(id)

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


# Get Reviews of Restaurant
@restaurant_routes.route('/<int:id>/reviews')
def all_reviews_of_restaurant(id):
    """
    Get all reviews of a restaurant by it's id, append the user info + reviewImage info to the reviews
    """

    all_reviews = Review.query.filter(Review.restaurant_id == id).all()
    all_reviews_dict = [review.to_dict() for review in all_reviews]

    for review in all_reviews_dict:

        # Query for the users for each review and review images for each review
        user_info = User.query.filter(User.id == review['user_id']).one()
        review_images = ReviewImage.query.filter(ReviewImage.review_id == review['id']).all()

        # Turn the python information into dictionaries to manipulate it into each review
        user_info_dict = user_info.to_dict()
        review_images_dict = [image.to_dict() for image in review_images]

        # Add to the review
        review['user_info'] = user_info_dict
        review['review_images'] = review_images_dict

    return {"Reviews": all_reviews_dict}


# Create a Review of a Restaurant
@restaurant_routes.route('/<int:id>/reviews', methods=['POST'])
@login_required
def create_review(id):
    """
    Create a review of a restaurant by it's id
    """
    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    # Query for the user info
    user_info = User.query.get(current_user.id)
    user_info_dict = user_info.to_dict()

    if form.validate_on_submit():

        newReview = Review(
            restaurant_id = id,
            user_id = current_user.id,
            # the variable review, must exactly match the key in frontend 'review' when creating newReview on the form Modal
            review = form.data["review"],
            rating = form.data["rating"]
        )

        db.session.add(newReview)

        # Adding the user info when creating a review, so that it renders with the user info instead of undefined
        new_review_dict = newReview.to_dict()
        new_review_dict['user_info'] = user_info_dict

        db.session.commit()

        return new_review_dict

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

# Add an Image to a spot
@restaurant_routes.route('/<int:id>/images', methods=['POST'])
def add_image_to_restaurant(id):
    """
    Add an image to a restaurant by it's id
    """

    print(' did it hit the backend &&&&&&&&&&&&&&&&&&&&')
    if "image" not in request.files:
        return {"errors": "image required"}, 400

    image = request.files["image"]

    if not allowed_file(image.filename):
        return {"errors": "file type not permitted"}, 400

    image.filename = get_unique_filename(image.filename)

    # if upload is successfuly will return a key "url" and the value is the url
    upload = upload_file_to_s3(image)

    if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message
        return upload, 400

    url = upload['url']

    restaurant_image = RestaurantImage(
        restaurant_id = id,
        url = url,
        preview = False
    )

    db.session.add(restaurant_image)
    db.session.commit()

    print('did it save and commit? ###################')
    # Query for restaurant
    restaurant = Restaurant.query.get(id)
    return restaurant.to_dict()
