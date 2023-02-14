"""
Van Nguyen
HasOffer API coding exercise.
4/7/2019
filename: abstract_database_connection.py
"""

import sqlite3

class AbstractDatabaseConnection():
    """
    This class manages the database connection.
    """
    def __init__(self, database):
        self.database = database
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.database)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
 