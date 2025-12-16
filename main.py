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
from movie_edit_form import MovieEditForm
from models.movie_queries import MovieQueries

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

movie_queries = MovieQueries()


@app.route("/")
def home():
    all_movies = movie_queries.get_all_movies()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_movie():

    global movie_to_edit
    form = MovieEditForm()

    if request.method == "POST":
        movie_id = request.args.get("id")
        print(f"===========> POST request, movie_id = {movie_id}")

        movie_to_edit = movie_queries.get_movie_by_id(movie_id)

        if form.validate_on_submit():
            new_rating = form.rating.data
            new_review = form.review.data

            print(new_rating, new_review)

            try:
                movie_to_edit.rating = new_rating
                movie_to_edit.review = new_review

                db.session.add(movie_to_edit)
                db.session.commit()

            except Exception as e:
                print(f"Error while editing the rating and review of movie = {e}")

            return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete")
def delete_movie():

    id = request.args.get("id")
    print(f"===========> DELETE request, id = {id}")

    movie_to_delete = movie_queries.get_movie_by_id(id)

    try:
        db.session.delete(movie_to_delete)
        db.session.commit()

        print(f"{movie_to_delete} has been deleted")
    except Exception as e:
        print(f"=================> Error while deleting movie = {e}")

    return redirect(url_for("home"))



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
