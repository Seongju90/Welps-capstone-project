from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, Regexp, URL
from datetime import datetime
from app.models import Restaurant


def phonenumber_exists(form, field):
    # Checking if the phone number exists
    phone_number = field.data
    restaurant = Restaurant.query.filter(Restaurant.phone_number == phone_number).first()
    if restaurant:
        raise ValidationError(message="Phone number already exists for a different restaurant")


def validate_start_hour(form, field):
    # form is what the user fills out, start_hour is the field, .data is used to access value that user entered
    start_hour_str = form.start_hours.data
    # field is object being validated, *where is the validator being placed, in which field*
    end_hour_str = field.data



    if len(start_hour_str) == 0 :
        raise ValidationError(message='Please input a starting hour for comparison')

    # Parse the strings into datetime objects,, %I:%M %p => 12 hour clock format, %I hours, %M minutes, %p AM/PM indicator
    start_hour = datetime.strptime(start_hour_str, '%I:%M %p').time()
    end_hour = datetime.strptime(end_hour_str, '%I:%M %p').time()

    # Compare the time objects
    if start_hour >= end_hour:
        raise ValidationError(message='Ending hour must be later than starting hour.')


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
            Regexp(r'^\d+\s+[a-zA-Z]+(?:\s+[a-zA-Z]+)*\s+(?:St(?:reet)?|Ave(?:nue)?|Rd(?:oad)?|Blvd(?:oulevard)?|Ln(?:ane)?|Dr(?:ive)?|Ct(?:ourt)?)?\.?\s*$',
                message='Must be a valid address in the following format: 1010 Kiely Blvd, no digits are allowed in street names')
            #  \d+ matches one or more digits, \s+ one or more whitespace
            # (?:\s+[a-zA-Z]+)* optional match for the optional second word
            # ? => quanitfier zero or one occurrences
            # * => quantifer zero or more occurrences
            # + => quantifier one or more occurrences
        ])
    city = StringField(
        "City",
        validators = [
            DataRequired("City is required"),
            Length(min=5, max=255, message='City must be 5 to 255 characters'),
            Regexp(r'^[a-zA-Z]+(?:\s+[a-zA-Z]+)?\s*$', message='City must only be alphabets')
            # The plus sign + means that the pattern should match one or more occurrences of the preceding character set.
        ])
    state = StringField(
        "State",
        validators = [
            DataRequired("State is required"),
            Regexp(r'^[A-Z]{2}\s*$', message='State must be two consecutive capital letters'),
            # r indicates raw string, because \ , \n can be use for new lines or escape characters
            # and in regex we use that, so it treats are literal characters, rather than escape character
            # custom_regex_validator(r'^[A-Z]{2}$', 'State must be two consecutive capital letters')
        ])
    country = StringField(
        "Country",
        validators = [
            DataRequired("Country is required"),
            Length(min=1, max=255, message='Country must be 1 to 255 characters'),
            Regexp(r'^[a-zA-Z]+(?:\s+[a-zA-Z]+)?\s*$', message='Country must only be alphabets')
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
            phonenumber_exists,
            Regexp(r'^\(?([0-9]{3})\)?[-.●/]?([0-9]{3})[-.●/]?([0-9]{4})$', message='Phone number must be in XXX-XXX-XXXX format')
            # \(? optional opening parenthesis, \)? option closing parenthesis
            # ([0-9]{3}) matches three digits in one group ()
            # [-.●]? optional separator
        ])
    preview_image = StringField(
        "Preview Image",
        validators = [
            DataRequired("Preview Image is required"),
            URL(require_tld=True, message="Invalid Url"),
            # If true, then the domain-name portion of the URL must contain a .tld suffix.
            # tld = top-level-domain => suffix that follows domain name in web address
            Regexp(r'^https?:\/\/(?:[a-z0-9\-]+\.)+[a-z]{2,}(?:\/[\w-]+)+(?:\.(?:jpe?g|gif|png))(?:\?.*)?$', message='Invalid image URL')
            # https?:\/\/ => matches the start of URL with http:// or with https://
            # (?:[a-z0-9\-]+\.)+ => Matches one or more domain name segments, separated by a dot. Each segment can contain lowercase letters or hyphens or numbers.
            # [a-z]{2,} => matches the top-level domain, which consists of two or more lowercase letters
            # (?:\/[\w-]+)+ => matches one or more path segments consisting of one or more word characters or hyphens separated by forward slashes.
            # (?:\.(?:jpe?g|gif|png)) => matches a file extension
            # (?:\?.*)? => matches optional query string at the end
        ])
    start_hours = StringField(
        "Start Hours",
        validators = [
            DataRequired("Starting hours is required"),
            Regexp(r'^(?:Open 24 hours|(?:0?[1-9]|1[012]):[0-5][0-9]\s(?:AM|PM|am|pm))\s*$', message='Start hours must be either the following format: Open 24 hours | XX:XX AM | XX: XX PM' ),
        ])
    end_hours = StringField(
        "End Hours",
        validators = [
            DataRequired("Ending hours is required"),
            Regexp(r'^(?:Open 24 hours|(?:0?[1-9]|1[012]):[0-5][0-9]\s(?:AM|PM|am|pm))\s*$', message='End hours must be either the following format: Open 24 hours | XX:XX AM | XX: XX PM' ),
            validate_start_hour
        ])
    submit = SubmitField("Add a Restaurant!")
