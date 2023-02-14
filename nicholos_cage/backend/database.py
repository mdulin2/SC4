"""
Maxwell Dulin 
Super Secure Library 
"""

# For whatever reason, the rendering engine of sqlite3 prevents a trivial SQLi in the login form. 
# But, MySQL is still vulnerable to this. So, this will be transitioning into a MySQL challenge. 
import sqlite3
from abstract_database_connection import AbstractDatabaseConnection


create_statements = {
    # Create statement for album table.
	'login_sql' : """CREATE TABLE login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
		password TEXT NOT NULL
    );""", 
	'session' : """CREATE TABLE IF NOT EXISTS session (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session TEXT NOT NULL
    );"""
	
}

insert_statements = {
    # Insert statement for album table.
    'author insert' : """INSERT INTO login(username,password) VALUES
        ("admin","admin")
		;"""
}

def create_tables():
    """
    Creates all tables in the database.
    """
    with AbstractDatabaseConnection('login.db') as conn:
        cursor = conn.cursor()
        for cs in create_statements:
            cursor.execute(create_statements[cs])
        conn.commit()

def seed():
    """
    Insert sample data to tables in the database.
    """
    with AbstractDatabaseConnection('login.db') as conn:
        cursor = conn.cursor()
        for ins in insert_statements:
            cursor.execute(insert_statements[ins])
        conn.commit()

def delete_tables():

	with AbstractDatabaseConnection('login.db') as conn:
		cursor = conn.cursor()
		cursor.execute("""DROP TABLE login""")
		conn.commit()	
	
def setup():
	"""
	Create and seed the database.
	"""
	delete_tables()
	create_tables()
	seed()

if __name__ == '__main__':
    setup()