import sqlite3
from flask import Flask, request, render_template, g

app = Flask(__name__)
DATABASE = 'library.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row 
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def search():
    results = None
    search_query_input = ""
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        search_query_input = book_id
        db = get_db()
        

        query = f"SELECT id, title, description, image_url FROM books WHERE id = {book_id}"
        
        try:
            cursor = db.execute(query)
            results = cursor.fetchall()
        except sqlite3.Error as e:
            results = f"Error: {e}"

    return render_template('index.html', results=results, last_input=search_query_input)

@app.cli.command('init-db')
def init_db_command():
    """Membuat tabel database baru dan menambahkan data dummy."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS books")

    cursor.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT NOT NULL
        );
    ''')

    books = [
        (1, 'The Art of Programming', 'A deep dive into computer science.', '/static/art programming.png'),
        (2, 'History of the Web', 'How the internet came to be.', '/static/history of the web.png'),
        (3, 'Cybersecurity Essentials', 'Protecting yourself in the digital age.', '/static/cybersecurity.png'),
        (4, 'Data Structures in Python', 'Mastering lists, dictionaries, and more.', '/static/data structure python.png'),
        (5, 'Introduction to Machine Learning', 'From linear regression to neural networks.', '/static/intro ml.png'),
        (6, 'The Ethical Hacker', 'A guide to penetration testing.', '/static/The ethical hacker.png'),
        (7, 'Cloud Computing Basics', 'Understanding AWS, Azure, and GCP.', '/static/cloud computing.png'),
        (8, 'Web Development with Flask', 'Build powerful web apps with Python.', '/static/web dev flask.png'),
        (9, 'Advanced SQL Queries', 'Unleash the power of your database.', '/static/advance sql.png'),
        (10, 'Cracking the Coding Interview', 'The ultimate guide for tech interviews.', '/static/interview.png'),
        (9999999999999, 'Secrets of the Library', 'ZmxhZ3tUaDFzXzFzX1kwdXJfUzNjcjN0X0ZsNGd9', '/static/secret.png')
    ]
    cursor.executemany("INSERT INTO books (id, title, description, image_url) VALUES (?, ?, ?, ?)", books)
    
    conn.commit()
    conn.close()
    print('Database perpustakaan telah diinisialisasi dengan data baru.')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5022)
