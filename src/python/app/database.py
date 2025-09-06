import sqlite3
import os

# Define the absolute path for the database in the project root
# This makes the path independent of where the script is run from
DB_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'calendar.db'))

def get_db_connection():
    """Creates and returns a database connection."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initializes the database and creates the events table if it doesn't exist."""
    print(f"Connecting to database at: {DB_FILE}")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                notified INTEGER NOT NULL DEFAULT 0
            );
        """)
        
        # Example of adding an index for faster queries on date
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_date ON events (date);")

        conn.commit()
        print("Database table 'events' is ready.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

def add_event(date, time, title, description):
    """Adds a new event to the database."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO events (date, time, title, description) VALUES (?, ?, ?, ?)",
            (date, time, title, description)
        )
        conn.commit()
        print(f"Added event: {title} on {date} at {time}")
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

def get_events_by_date(date):
    """Retrieves all events for a specific date."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM events WHERE date = ? ORDER BY time", (date,))
        # Return results as a list of dictionaries
        return [dict(row) for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

def delete_event(event_id):
    """Deletes an event from the database by its ID."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
        conn.commit()
        print(f"Deleted event with ID: {event_id}")
        return cursor.rowcount > 0  # Returns True if a row was deleted
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

if __name__ == '__main__':
    # This allows us to run this script directly to set up the database
    print("Running database initialization...")
    init_database()
