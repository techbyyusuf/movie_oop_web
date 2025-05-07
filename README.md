# 🎬 MovieApp (OOP + Web)

A command-line movie manager that lets you add, view, delete, and manage your favorite movies. It also fetches movie data using the OMDb API and generates a beautiful static HTML website with posters and details.

---

## 📁 Project Structure

```
Movie_oop_web/
│
├── main.py                   # Entry point of the application
├── index.html                # Generated movie website (static)
├── .env                      # Stores your OMDb API key
├── requirements.txt          # Python dependencies
│
├── app/                      # Core app logic
│   ├── movie_app.py          # Menu, user commands, etc.
│   └── omdb_helper.py        # Function to load movie data from OMDb API
│
├── storage/                  # Storage interface + implementations
│   ├── __init__.py
│   ├── istorage.py           # Interface definition
│   ├── storage_json.py       # JSON storage
│   └── storage_csv.py        # CSV storage
│
├── data/                     # Your local movie databases
│   ├── movies.json
│   ├── my_movies.json
│   └── movies.csv
│
├── templates/                # HTML template(s)
│   └── index_template.html
│
└── _static/                  # Styling and assets
    ├── style.css
    └── default.jpg           # Optional placeholder for missing posters
```

---

## 🚀 Features

- Add movies (only title required – info fetched via OMDb API)
- List all movies
- Delete and update movies
- View stats (count, average rating, etc.)
- Random movie picker
- Search by title
- Sort by rating
- Generate a static HTML website
- Open the website in your browser

---

## 🧪 Setup Instructions

### 1. Clone the project and create a virtual environment

```bash
git clone https://github.com/techbyyusuf/movie_oop_web.git
cd Movie_oop_web
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your OMDb API key

Create a `.env` file in the project root and insert your API key:

```
API_KEY=your_api_key_here
```

You can get one for free from: https://www.omdbapi.com/apikey.aspx

---

## 🖥️ Run the Application

```bash
python main.py
```

Use the interactive menu to manage your movie collection.

---

## 🌐 Generated Website

- Use menu option `9` to generate the static website.
- Use menu option `10` to open the site in your default browser.
- The site uses `templates/index_template.html` as a base and saves the result as `index.html`.

---

## ✅ Requirements

```
matplotlib
numpy
rapidfuzz
colorama
python-dotenv
requests
```

(Already included in `requirements.txt`)

---

## 📄 License

MIT License
