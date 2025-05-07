from app.movie_app import MovieApp
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCsv


def main():
    """
    Creates the storage and movie app, then runs it.
    """
    storage = StorageJson("data/movies.csv")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
