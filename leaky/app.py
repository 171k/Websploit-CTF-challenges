import sqlite3
from flask import Flask, request, render_template, g

app = Flask(__name__)
DATABASE = 'leaderboard.db'

# --- Database Setup ---
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

# --- Main Application Route ---
@app.route('/', methods=['GET', 'POST'])
def view_leaderboard():
    results = None
    error_message = None
    query_input = ""

    if request.method == 'POST':
        player_rank = request.form.get('player_rank')
        query_input = player_rank
        db = get_db()
        
        # --- !!! VULNERABLE CODE !!! ---
        # Query is built directly from user input.
        # The try-except block leaks database errors to the user.
        query = f"SELECT rank, username, score FROM leaderboard WHERE rank = {player_rank}"
        
        try:
            cursor = db.execute(query)
            results = cursor.fetchall()
            if not results:
                error_message = "No player found at that rank."
        except sqlite3.Error as e:
            # This leak is the core of the vulnerability.
            error_message = f"Database Error: {e}"

    return render_template('index.html', results=results, error=error_message, last_input=query_input)

# --- Database Initialization Command ---
@app.cli.command('init-db')
def init_db_command():
    """Creates the database tables and populates them with data."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS leaderboard")
    cursor.execute("DROP TABLE IF EXISTS internal_flags")
    
    # Create the leaderboard table
    cursor.execute('''
        CREATE TABLE leaderboard (
            id INTEGER PRIMARY KEY,
            rank INTEGER NOT NULL,
            username TEXT NOT NULL,
            score INTEGER NOT NULL
        );
    ''')
    
    # Create a secret table for the flag
    cursor.execute('''
        CREATE TABLE internal_flags (
            id INTEGER PRIMARY KEY,
            secret_value TEXT NOT NULL
        );
    ''')
    
    # Add dummy leaderboard data
    leaderboard_data = [
        (1, 'CyberNinja', 99500),
        (2, 'GlitchHunter', 98700),
        (3, 'DataDragon', 95100),
        (4, 'SyntaxSlayer', 92300),
        (5, 'KernelKing', 90800)
    ]
    cursor.executemany("INSERT INTO leaderboard (rank, username, score) VALUES (?, ?, ?)", leaderboard_data)

    # Insert the flag into the secret table
    cursor.execute("INSERT INTO internal_flags (secret_value) VALUES ('flag{L34ky_L34d3rb04rd_S3cr3t}')")
    
    conn.commit()
    conn.close()
    print('🏆 Leaderboard database initialized.')

if __name__ == '__main__':
    app.run(debug=True, port=5021, host="0.0.0.0")
