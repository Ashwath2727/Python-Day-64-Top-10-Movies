from urllib.parse import quote

import sqlalchemy
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

from extensions import db
from models.movies import Movie

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = quote("ashwath@MVN123")
DB_HOST = "localhost"

SQLALCHEMY_DB_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DB_URI
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)


@app.route("/")
def home():
    global all_movies
    try:
        print("==================> Getting all movies")
        all_movies = Movie.query.all()
        print(all_movies)
    except Exception as e:
        print(f"Error Getting records = {e}")
    return render_template("index.html", movies=all_movies)


if __name__ == '__main__':
    with app.app_context():
        print("===========================> Creating tables")
        db.create_all()
        print("============================> Finished Creating tables")

        # try:
        #     print("======================> adding 1st movie")
        #     new_movie = Movie(
        #         title="Phone Booth",
        #         year=2002,
        #         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        #         rating=7.3,
        #         ranking=10,
        #         review="My favourite character was the caller.",
        #         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        #     )
        #
        #     db.session.add(new_movie)
        #     db.session.commit()
        #     print("=========================> finished adding 1st movie")
        #
        # except sqlalchemy.exc.IntegrityError as e:
        #     print("=================> 1st movie is already in the table")

        # try:
        #     print("========================> adding 2nd movie")
        #     second_movie = Movie(
        #         title="Avatar The Way of Water",
        #         year=2022,
        #         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        #         rating=7.3,
        #         ranking=9,
        #         review="I liked the water.",
        #         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
        #     )
        #
        #     db.session.add(second_movie)
        #     db.session.commit()
        #     print("========================> finished adding 2nd movie")
        #
        # except sqlalchemy.exc.IntegrityError as e:
        #     print("=================> 2nd movie is already in the table")

    app.run(debug=True)
