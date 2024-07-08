from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import string
import random

app = Flask(__name__)
DATABASE = 'database.db'

# Function to generate a random short code


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Initialize the database


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                long_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()

# Fetch recent URLs


def get_recent_urls():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT long_url, short_code FROM urls ORDER BY id DESC LIMIT 5')
        return cursor.fetchall()

# Home route to submit long URLs


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO urls (long_url, short_code) VALUES (?, ?)', (long_url, short_code))
            conn.commit()

        return render_template('short_url.html', short_code=short_code)

    recent_urls = get_recent_urls()
    return render_template('index.html', recent_urls=recent_urls)

# Redirect route for short URLs


@app.route('/<short_code>')
def redirect_url(short_code):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT long_url FROM urls WHERE short_code = ?', (short_code,))
        result = cursor.fetchone()

        if result:
            return redirect(result[0])
        else:
            return render_template('error.html')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
