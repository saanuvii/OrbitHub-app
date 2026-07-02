# NASA Space Explorer 🚀

A modern, responsive, and beautifully designed full-stack web application that interacts with various NASA Open APIs. Build with Python, Flask, and Bootstrap 5.

## 🌟 Features

- **Astronomy Picture of the Day (APOD):** View daily HD images or videos from space with detailed explanations.
- **Mars Rover Photos:** Explore images taken by Curiosity, Opportunity, Spirit, and Perseverance on the Red Planet. Filter by Earth date and specific cameras.
- **Near Earth Asteroids:** Keep track of objects approaching Earth, complete with hazard warnings and speed data.
- **Space Weather Dashboard:** Monitor solar flares, geomagnetic storms, and coronal mass ejections.
- **Favorites System:** Save your favorite images, rovers, and asteroids using a database.
- **Search Capabilities:** Basic routing search for specific dates or rover names.
- **Premium UI:** Space-themed dark mode, glassmorphism UI elements, smooth animations, and toast notifications.

## 📸 Screenshots

*(Add screenshots here)*
- `home.png`
- `apod.png`
- `mars.png`

## 🛠️ Technologies Used

### Backend
- Python 3
- Flask
- Flask-SQLAlchemy (Database ORM)
- Flask-Caching
- Requests

### Frontend
- HTML5 / CSS3 (Custom Glassmorphism styling)
- Bootstrap 5
- JavaScript (Vanilla)
- Font Awesome

## 📁 Folder Structure

```
NASA-Space-Explorer/
│
├── app.py                 # Application entry point & setup
├── config.py              # Configuration variables
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
│
├── static/
│   ├── css/style.css      # Custom styling and animations
│   ├── js/main.js         # Frontend interactivity
│   └── images/
│
├── templates/             # Jinja2 HTML templates
│   ├── base.html          # Main layout wrapper
│   ├── index.html
│   ├── apod.html
│   ├── mars.html
│   ├── asteroids.html
│   ├── weather.html
│   ├── favorites.html
│   ├── about.html
│   └── errors/            # Custom error pages
│
├── database/
│   └── models.py          # SQLAlchemy Models (Favorites)
│
├── utils/
│   └── nasa_api.py        # Logic for fetching from NASA APIs
│
└── routes/                # Flask Blueprints
    ├── main.py
    ├── apod.py
    ├── mars.py
    ├── asteroids.py
    ├── weather.py
    ├── favorites.py
    └── search.py
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd NASA-Space-Explorer
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   The `.env` file is included, but for production or higher rate limits, get an API key from [api.nasa.gov](https://api.nasa.gov/) and update `NASA_API_KEY` in `.env`.
   To use Supabase or another PostgreSQL provider, add:
   `DATABASE_URL=postgresql://[user]:[password]@[host]:[port]/[db]`
   *(If not provided, it falls back to a local SQLite database in the `database/` folder).*

5. **Run the application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 🔮 Future Improvements

- Fully implement user authentication (Registration/Login).
- Add infinite scrolling to the Mars Rover photos.
- Implement an image slideshow for APOD history.
- Set up a Redis cache for improved API caching performance.
- Expand Global Search logic with a local Elasticsearch index or database cache of previous queries.

## 📄 License

This project is open-source and available under the MIT License.
