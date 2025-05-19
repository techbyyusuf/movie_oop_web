from abc import ABC, abstractmethod

class IStorage(ABC):
    """
    Interface for movie storage implementations.
    Any storage class (e.g. JSON, CSV, database) must implement these methods
    to handle adding, listing, updating, and deleting movie entries.
    """

    @abstractmethod
    def list_movies(self):
        """
        Returns all movies as a dictionary.
        Keys are movie titles, values are dictionaries with movie information.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the storage.
        Args:
            title (str): Title of the movie.
            year (str or int): Release year.
            rating (str or float): Rating of the movie.
            poster (str): URL or identifier for the movie poster.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie by title (case-insensitive).
        Args:
            title (str): Title of the movie to delete.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Updates the rating of a movie by title (case-insensitive).
        Args:
            title (str): Title of the movie to update.
            rating (str or float): New rating to assign.
        """
        pass
