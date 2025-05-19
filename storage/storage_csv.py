import csv
from .istorage import IStorage


class StorageCsv(IStorage):
    """
    Handles movie storage using a CSV file.
    Supports listing, adding, updating, and deleting movies.
    Titles are matched case-insensitively.
    """
    def __init__(self, file_path):
        """
        Stores the path to the CSV file.
        """
        self.file_path = file_path


    def list_movies(self):
        """
        Reads all movies from CSV and returns them as a dictionary.
        """
        movies = {}
        try:
            with open(self.file_path, "r", newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    title = row["title"]
                    movies[title] = {
                        "rating": row["rating"],
                        "year": row["year"],
                        "poster": row.get("poster", "")
                    }
        except FileNotFoundError:
            pass
        except csv.Error as e:
            print(f"CSV parsing error: {e}")
        return movies


    def _find_title(self, movies, title):
        """
        Helper method to find the exact movie key.
        """
        return next(
            (movie for movie in movies if movie.lower() == title.lower()), None)


    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the CSV file if it doesn't already exist.
        """
        movies = self.list_movies()

        if self._find_title(movies, title):
            print(f"Movie '{title}' already exists!")
            return

        try:
            with open(self.file_path, "a", newline='') as f:
                writer = csv.writer(f)
                if f.tell() == 0:
                    writer.writerow(["title", "rating", "year", "poster"])
                writer.writerow([title, rating, year, poster])
            print(f"Movie '{title}' added.")
        except (OSError, csv.Error) as e:
            print(f"An error occurred while adding the movie: {e}")


    def _write_all_movies(self, movies):
        """
        Writes all movies back to the CSV file.
        """
        try:
            with open(self.file_path, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["title", "rating", "year", "poster"])
                for title, info in movies.items():
                    writer.writerow([
                        title,
                        info.get("rating", ""),
                        info.get("year", ""),
                        info.get("poster", "")
                    ])
        except (OSError, csv.Error) as e:
            print(f"An error occurred while saving the movies: {e}")


    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file if it exists.
        """
        movies = self.list_movies()
        matched_title = self._find_title(movies, title)

        if not matched_title:
            print(f"{title} not found in movie list!")
            return

        try:
            del movies[matched_title]
            self._write_all_movies(movies)
            print(f"{matched_title} deleted!")
        except (OSError, csv.Error) as e:
            print(f"An error occurred while saving the updated movie list: {e}")


    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the CSV file.
        """
        movies = self.list_movies()
        matched_title = self._find_title(movies, title)

        if not matched_title:
            print(f"{title} not found in movie list!")
            return

        try:
            movies[matched_title]["rating"] = str(rating)
            self._write_all_movies(movies)
            print(f"{matched_title} updated!")
        except (OSError, csv.Error) as e:
            print(f"An error occurred while saving the updated movie list: {e}")
