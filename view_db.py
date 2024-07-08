import sqlite3

DATABASE = 'database.db'


def view_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM urls')
        rows = cursor.fetchall()

        if rows:
            print("id | long_url | short_code")
            print("-" * 40)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]}")
        else:
            print("No data found.")


if __name__ == '__main__':
    view_data()
