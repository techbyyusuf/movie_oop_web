import csv
from .istorage import IStorage


class StorageCsv(IStorage):
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
                        "Rating": row["rating"],
                        "Year": row["year"],
                        "Poster": row.get("poster", "")
                    }
        except FileNotFoundError:
            pass
        return movies


    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the CSV file if it doesn't exist.
        """
        movies = self.list_movies()
        if title in movies:
            print(f"Movie '{title}' already exists!")
            return

        with open(self.file_path, "a", newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(["title", "rating", "year", "poster"])
            writer.writerow([title, rating, year, poster])


    def _write_all_movies(self, movies):
        """
        Writes all movies back to the CSV file.
        """
        with open(self.file_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["title", "rating", "year", "poster"])
            for title, info in movies.items():
                writer.writerow([
                    title,
                    info.get("Rating", ""),
                    info.get("Year", ""),
                    info.get("Poster", "")
                ])


    def delete_movie(self, title):
        """
        Deletes a movie from the CSV file if it exists.
        """
        movies = self.list_movies()
        if title not in movies:
            print(f"{title} not found in movie list!")
            return

        del movies[title]
        self._write_all_movies(movies)


    def update_movie(self, title, rating):
        """
        Updates the rating of a movie in the CSV file.
        """
        movies = self.list_movies()
        if title not in movies:
            print(f"{title} not found in movie list!")
            return

        movies[title]["Rating"] = str(rating)
        self._write_all_movies(movies)
