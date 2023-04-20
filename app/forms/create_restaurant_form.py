from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp
# importing re module to  use the match method in my regex custom validator
import re
from app.models import Restaurant


def phonenumber_exists(form, field):
    # Checking if the phone number exists
    phone_number = field.data
    restaurant = Restaurant.query.filter(Restaurant.phone_number == phone_number).first()
    if restaurant:
        raise ValidationError("Phone number already exists for a different restaurant")


# def custom_regex_validator(regex_pattern, message=None):
#     """
#     Custom validator that checks if field matches the regex pattern inserted.
#     """
#     # re.compile => compiles the regex pattern into a regular expression object in order to use
#     # match() or search() methods
#     regex = re.compile(regex_pattern)

#     def validate(form, field):
#         message = message or None
#         if not regex.match(field.data):
#             message = message or f'Invalid input: {field.data}'
#         if message is not None:
#             raise ValidationError(message)

#     return validate


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
            Length(min=5, max=255, message='Address must be 5 to 255 characters'),
            Regexp(r'^\d+\s+[a-zA-Z]+(?:\w+\s)?\w+\s+(?:St|Street|Ave|Avenue|Rd|Road|Blvd|Boulevard|Ln|Lane|Dr|Drive|Ct|Court)\.?\s*$',
                message='Must be a valid address in the following format: 1010 Kiely Blvd')
            # (?: etc) non-capturin group that matches any of the common street types
            #  \d+ matches one or more digits, \s+ one or more whitespace
            # (?:\w+\s)? optional non-capturing group, for street names with two letters Queen Anne
        ])
    city = StringField(
        "City",
        validators = [
            DataRequired("City is required"),
            Length(min=5, max=255, message='City must be 5 to 255 characters'),
            Regexp(r'[a-z,A-Z,\s]+', message='City must only be alphabets')
            # The plus sign + means that the pattern should match one or more occurrences of the preceding character set.
        ])
    state = StringField(
        "State",
        validators = [
            DataRequired("State is required"),
            Regexp(r'^[A-Z]{2}$', message='State must be two consecutive capital letters'),
            # r indicates raw string, because \ , \n can be use for new lines or escape characters
            # and in regex we use that, so it treats are literal characters, rather than escape character
            # custom_regex_validator(r'^[A-Z]{2}$', 'State must be two consecutive capital letters')
        ])
    country = StringField(
        "Country",
        validators = [
            DataRequired("Country is required"),
            Length(min=1, max=255, message='Country must be 1 to 255 characters'),
            Regexp(r'[a-z,A-Z,\s]+', message='Country must only be alphabets')
        ])
    zipcode = StringField(
        "Zipcode",
        validators = [
            DataRequired("Zipcode is required"),
            Regexp(r'^\d{5}(?:[-\s]\d{4})?$', message='Zipcode must be in XXXXX or XXXXX-XXXX format')
            # (?:[-\s]\d{4})? optional non-capturing group that matches either a hyphen or whitespace character, followed by exactly 4 digits.
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
