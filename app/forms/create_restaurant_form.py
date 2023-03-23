from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import Restaurant


def phonenumber_exists(form, field):
    # Checking if the phone number exists
    phone_number = field.data
    restaurant = Restaurant.query.filter(Restaurant.phone_number == phone_number).first()
    if restaurant:
        raise ValidationError("Phone number already exists for a different restaurant")


class RestaurantForm(FlaskForm):
    name = StringField(
        "Restaurant Name",
        validators = [
            DataRequired("Restaurant name is required"),
            Length(min=5, max=255, message='Name must be 5 to 255 characters')
        ])
    address = StringField(
        "Address",
        validators = [
            DataRequired("Address is required"),
            Length(min=5, max=255, message='Address must be 5 to 255 characters')
        ])
    city = StringField(
        "City",
        validators = [
            DataRequired("City is required"),
            Length(min=5, max=255, message='City must be 5 to 255 characters')
        ])
    state = StringField(
        "State",
        validators = [
            DataRequired("State is required"),
            Length(min=2, max=2, message='State must be two characters')
        ])
    country = StringField(
        "Country",
        validators = [
            DataRequired("Country is required"),
            Length(min=5, max=255, message='Country must be 5 to 255 characters')
        ])
    zipcode = IntegerField(
        "Zipcode",
        validators = [
            DataRequired("Zipcode is required"),
        ])
    price = SelectField(
        "Price Range",
        choices = [
            "$",
            "$$",
            "$$$",
            "$$$$"
        ],
        validators = [
            DataRequired("Price Range is required")
        ])
    phone_number = StringField(
        "Phone Number",
        validators = [
            DataRequired("Phone number is required"),
            phonenumber_exists
        ])
    preview_image = StringField(
        "Preview Image",
        validators = [
            DataRequired("Preview Image is required"),
        ])
    start_hours = StringField(
        "Start Hours",
        validators = [
            DataRequired("Starting hours is required"),
        ])
    end_hours = StringField(
        "End Hours",
        validators = [
            DataRequired("Ending hours is required"),
        ])
    submit = SubmitField("Add a Restaurant!")
