import json
from .istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        Stores the path to the file where movies are saved.
        """
        self.file_path = file_path


    def list_movies(self):
        """
        Reads all movies from the file and returns them.
        If file is empty or broken, returns empty dict.
        """
        try:
            with open(self.file_path, "r") as f:
                movies = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            movies = {}
        return movies


    def _save_movies(self, movies):
        """
        Saves the current movie list to the file.
        """
        with open(self.file_path, "w") as f:
            json.dump(movies, f, indent=4)


    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the list if it doesn't already exist.
        """
        movies = self.list_movies()
        if title in movies:
            print(f"Movie '{title}' already exists!")
        else:
            movies[title] = {
                "Year": str(year),
                "Rating": str(rating),
                "Poster": poster
            }
            self._save_movies(movies)


    def delete_movie(self, title):
        """
        Deletes a movie if it exists in the list.
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
        else:
            print(f"{title} not found in movie list!")


    def update_movie(self, title, rating):
        """
        Updates the rating of a movie.
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]["Rating"] = str(rating)
            self._save_movies(movies)
        else:
            print(f"{title} not found in movie list!")
