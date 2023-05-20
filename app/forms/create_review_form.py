from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class ReviewForm(FlaskForm):
    review = StringField(
        "Review",
        validators = [
            DataRequired("Review is required")
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
