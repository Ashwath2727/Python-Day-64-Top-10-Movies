from models.movies import Movie


class MovieQueries:

    def get_all_movies(self):
        global all_movies
        try:
            print("==================> Getting all movies")
            all_movies = Movie.query.order_by(Movie.rating).all()
            print(all_movies)
        except Exception as e:
            print(f"Error Getting records = {e}")

        return all_movies

    def get_movie_by_id(self, movie_id):
        global movie_to_edit
        try:
            movie_to_edit = Movie.query.filter_by(id=movie_id).all()[0]
            print(f"movie_to_edit = {movie_to_edit}")
        except Exception as e:
            print(f"Error Getting records = {e}")

        return movie_to_edit