import json
from .istorage import IStorage


class StorageJson(IStorage):
    """
    Handles movie storage using a JSON file.
    Supports listing, adding, updating, and deleting movies.
    Titles are matched case-insensitively.
    """

    def __init__(self, file_path):
        """Initializes the JSON storage with a given file path."""
        self.file_path = file_path

    def list_movies(self):
        """Reads all movies from the file and returns them as a dict."""
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
        except Exception as e:
            print(f"Unexpected error while reading movies: {e}")
            return {}

    def _save_movies(self, movies):
        """Saves the movie dictionary to the file."""
        try:
            with open(self.file_path, "w") as f:
                json.dump(movies, f, indent=4)
        except (OSError, TypeError) as e:
            print(f"Error saving movies: {e}")

    def _find_title(self, movies, title):
        """Helper method to find the exact movie key."""
        return next((movie for movie in movies if movie.lower() == title.lower()), None)

    def add_movie(self, title, year, rating, poster):
        """Adds a new movie if it doesn't already exist."""
        movies = self.list_movies()
        if self._find_title(movies, title):
            print(f"Movie '{title}' already exists!")
            return

        movies[title] = {
            "year": str(year),
            "rating": str(rating),
            "poster": poster
        }
        self._save_movies(movies)
        print(f"Movie '{title}' added.")

    def delete_movie(self, title):
        """Deletes a movie if it exists."""
        movies = self.list_movies()
        matched_title = self._find_title(movies, title)
        if not matched_title:
            print(f"'{title}' not found in movie list!")
            return

        try:
            del movies[matched_title]
            self._save_movies(movies)
            print(f"'{matched_title}' deleted.")
        except Exception as e:
            print(f"Error deleting movie: {e}")

    def update_movie(self, title, rating):
        """Updates the rating of a movie."""
        movies = self.list_movies()
        matched_title = self._find_title(movies, title)
        if not matched_title:
            print(f"'{title}' not found in movie list!")
            return

        try:
            movies[matched_title]["rating"] = str(rating)
            self._save_movies(movies)
            print(f"'{matched_title}' updated.")
        except Exception as e:
            print(f"Error updating movie: {e}")
