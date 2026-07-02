# OrbitHub 🚀

A modern, responsive, and beautifully designed full-stack web application that interacts with various NASA Open APIs. Build with Python, Flask, and Bootstrap 5.

## 🌟 Features

- **Astronomy Picture of the Day (APOD):** View daily HD images or videos from space with detailed explanations.
- **Near Earth Asteroids:** Keep track of objects approaching Earth, complete with hazard warnings and speed data.
- **Space Weather Dashboard:** Monitor solar flares, geomagnetic storms, and coronal mass ejections.
- **Search Capabilities:** Basic routing search for specific dates.
- **Premium UI:** Space-themed dark mode, glassmorphism UI elements, smooth animations, and toast notifications.

## ⚠️ Getting your own NASA API Key

NASA strictly limits the use of the `DEMO_KEY` to **30 requests per IP address per hour** and **50 requests per day**. If you see "Rate Limit Exceeded" messages on the website, you must provide your own API key.

1. Go to [https://api.nasa.gov/](https://api.nasa.gov/)
2. Fill out the **Generate API Key** form.
3. Once you receive your key, go to the Render Dashboard for your deployment.
4. Click **Environment**.
5. Update the `NASA_API_KEY` variable from `DEMO_KEY` to your new 40-character key.
6. Save the changes. The app will automatically redeploy with the unlocked rate limits!

## 📸 Screenshots

*(Add screenshots here)*
- `home.png`
- `apod.png`
- `asteroids.png`

## 🛠️ Technologies Used

### Backend
- Python 3
- Flask
- Flask-Caching
- Requests

### Frontend
- HTML5 / CSS3 (Custom Glassmorphism styling, Space Grotesk font)
- Bootstrap 5
- JavaScript (Vanilla)
- Font Awesome

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd OrbitHub-app
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
   Create a `.env` file and set `NASA_API_KEY`.

5. **Run the application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

## 🔮 Future Improvements

- Add infinite scrolling to the dashboards.
- Implement an image slideshow for APOD history.
- Expand Global Search logic with a local Elasticsearch index or database cache of previous queries.

## 📄 License

This project is open-source and available under the MIT License.
