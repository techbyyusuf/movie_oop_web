import os
import random
import webbrowser

from app.omdb_helper import load_movie_data


class MovieApp:
    """
    Command-line interface for managing a movie collection.
    Allows the user to list, add, delete, update, search, and sort movies.
    Also supports generating and opening a website from stored movie data.
    This app relies on a storage object that implements the IStorage interface.
    """
    def __init__(self, storage):
        """
        Takes a storage object that follows the IStorage interface.
        """
        self._storage = storage
        self._menu_options = {
            "1": self._command_list_movies,
            "2": self._command_add_movie,
            "3": self._command_delete_movie,
            "4": self._command_update_movie,
            "5": self._command_movie_stats,
            "6": self._command_random_movie,
            "7": self._command_search_movie,
            "8": self._command_sort_by_rating,
            "9": self._generate_website,
            "10": self._command_open_website,
            "0": exit
        }

    def _command_list_movies(self):
        """
        Prints all movies from storage.
        """
        movies = self._storage.list_movies()
        print(f"{len(movies)} movies in total")
        for title, info in movies.items():
            print(f"\n{title}")
            for key, value in info.items():
                print(f"{key}: {value}")

    def _command_add_movie(self):
        """
        Asks for movie title, fetches info from OMDb, and adds the movie.
        """
        title = input("Enter movie title: ")
        data = load_movie_data(title)

        if data is None:
            print("Could not add movie.")
            return

        year = data['Year']
        rating = data['imdbRating']
        poster = data['Poster']
        self._storage.add_movie(title, year, rating, poster)
        print("Movie added!")

    def _command_delete_movie(self):
        """
        Asks user for a title and deletes the movie.
        """
        title = input("Enter movie title to delete: ")
        movies = self._storage.list_movies()
        if any(title.lower() == movie.lower() for movie in movies):
            self._storage.delete_movie(title)
            print("Movie deleted!")
        else:
            print("Movie not found.")

    def _command_update_movie(self):
        """
        Asks user for a title and new rating and updates the movie.
        """
        title = input("Enter movie title to update: ")
        rating = input("Enter new rating: ")
        self._storage.update_movie(title, rating)
        print("Movie updated!")

    def _command_movie_stats(self):
        """
        Shows average and total count of movies.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies in database.")
            return
        ratings = [float(info["rating"]) for info in movies.values()]
        avg = sum(ratings) / len(ratings)
        print(f"Average rating: {avg:.1f}")

    def _command_random_movie(self):
        """
        Picks and prints one random movie from the list.
        """
        movies = self._storage.list_movies()
        if not movies:
            print("No movies found.")
            return
        title, info = random.choice(list(movies.items()))
        print(f"\n🎲 Random movie: {title}")
        print(f"Rating: {info['rating']}")
        print(f"Year: {info['year']}")

    def _command_search_movie(self):
        """
        Searches for movies that contain a word in the title.
        """
        search = input("Search title: ").lower()
        found = False
        for title, info in self._storage.list_movies().items():
            if search in title.lower():
                print(f"\n{title}")
                print(f"Rating: {info['rating']}")
                print(f"Year: {info['year']}")
                found = True
        if not found:
            print("No matching movie found.")

    def _command_sort_by_rating(self):
        """
        Displays all movies sorted from best to worst rating.
        """
        movies = self._storage.list_movies()
        sorted_movies = sorted(
            movies.items(),
            key=lambda x: float(x[1]["rating"]),
            reverse=True
        )
        for title, info in sorted_movies:
            print(f"\n{title}")
            print(f"Rating: {info['rating']}")
            print(f"Year: {info['year']}")

    def _generate_website(self):
        """
        Generates a website with all movies and saves it as index.html.
        """
        try:
            with open("templates/index_template.html", "r", encoding="utf-8") as f:
                template = f.read()

            movies = self._storage.list_movies()

            movie_grid_html = ""
            for title, info in movies.items():
                poster = info.get("poster", "")
                year = info.get("year", "N/A")

                movie_html = f"""
                    <li>
                        <div class="movie">
                            <img class="movie-poster" src="{poster}" />
                            <div class="movie-title">{title}</div>
                            <div class="movie-year">{year}</div>
                        </div>
                    </li>
                """

                movie_grid_html += movie_html

            template = template.replace("__TEMPLATE_TITLE__", "My Movie Website")
            template = template.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)

            with open("index.html", "w", encoding="utf-8") as f:
                f.write(template)

            print("Website was generated successfully.")
        except Exception as e:
            print("Something went wrong while generating the website:", e)

    def _command_open_website(self):
        """
        Opens the generated index.html in the default web browser.
        """
        try:
            path = os.path.abspath("index.html")
            webbrowser.open("file://" + path)
            print("Opening website in the browser...")
        except Exception as e:
            print("Could not open website:", e)

    def _print_menu(self):
        """
        Prints the menu options.
        """
        print("""
        Menu:
        0. Exit
        1. List movies
        2. Add movie
        3. Delete movie
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating
        9. Generate website
        10. Open website
        """)

    def run(self):
        """
        Shows menu and handles user input.
        """
        while True:
            self._print_menu()
            choice = input("Choose an option: ")
            action = self._menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice.")
