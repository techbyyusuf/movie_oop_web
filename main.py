from app.movie_app import MovieApp
from storage.storage_json import StorageJson
from storage.storage_csv import StorageCsv


def main():
    """
    Creates the storage and movie app, then runs it.
    """
    #storage = StorageCsv("data/movies.csv")
    storage = StorageJson("data/movies.json")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
