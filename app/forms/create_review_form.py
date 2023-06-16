from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class ReviewForm(FlaskForm):
    review = StringField(
        "Review",
        validators = [
            DataRequired("Review is required"),
            Length(min=10, max=255, message='Review must be 10 to 255 characters')
        ]
    )
    rating = IntegerField(
        "Rating",
        validators = [
            DataRequired("Rating is required"),
            NumberRange(min=1, max=5, message="Rating must be between 1 and 5")
        ]
    )
    submit = SubmitField("Leave a Review!")
