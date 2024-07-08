# URL_shortener (The project is in the master branch)
This project is a simple URL shortener web application built with Flask and SQLite. It allows users to shorten long URLs into more manageable, user-friendly links. The application stores these links in a database and provides the functionality to redirect users to the original URL when they visit the shortened link.

Features
Shorten URLs: Enter a long URL to generate a unique short code.
Redirect to Original URL: Use the short code to redirect to the original long URL.
Recent URLs: Display a list of recently shortened URLs.
Error Handling: Gracefully handles non-existent short codes with an error page.
Responsive Design: User-friendly interface with responsive design.

Project Structure
graphql
Copy code
url_shortener/
│
├── app.py               # Main Flask application
├── view_db.py           # Script to view database contents
├── templates/           # HTML templates
│   ├── index.html       # Homepage template
│   ├── short_url.html   # Template to display shortened URL
│   └── error.html       # Error page template
├── static/              # Static files (CSS, JS, images)
│   └── style.css        # CSS file for styling
└── database.db          # SQLite database file

Setup and Usage
Clone the Repository:
git clone https://github.com/yourusername/url_shortener.git
cd url_shortener


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt

Run the Application:
python app.py

View Database Contents:
python view_db.py

Open in Browser:
Go to http://127.0.0.1:5000/ in your web browser.
