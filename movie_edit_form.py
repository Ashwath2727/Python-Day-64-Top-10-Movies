from flask_wtf import FlaskForm
from wtforms import FloatField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MovieEditForm(FlaskForm):

    rating = FloatField('Your Rating Out of 10 e.g 7.5', validators=[DataRequired()], name="new_rating")
    review = TextAreaField('Your Review', validators=[DataRequired()], name="new_review")

    submit = SubmitField('Submit')