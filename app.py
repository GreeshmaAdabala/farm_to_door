import sqlite3

def get_db_connection():
    conn = sqlite3.connect("farm.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row  # So rows behave like dictionaries
    return conn

def verify_farmer_login(name, password):
    # Only allow greeshma / greeshma
    if name == "Greeshma" and password == "greeshma":
        return {"name": "Greeshma"}  # simulate a valid farmer object
    else:
        return None
