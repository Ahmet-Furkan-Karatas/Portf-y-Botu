import sqlite3
from config import DATABASE

conn = sqlite3.connect('portföy.db')

cur = conn.cursor()

class DB_Manager:
    def __init__(self, database):
        self.database = database # veri tabanının adı
        
    def create_tables(self):
        pass

import sqlite3
from config import DATABASE

conn = sqlite3.connect('portföy.db')
cur = conn.cursor()

class DB_Manager:
    def __init__(self, database):
        self.database = database  # Veri tabanının adı
    
    def create_tables(self):
        pass

    cur.execute('''CREATE TABLE IF NOT EXISTS projects (
        project_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        project_name TEXT,
        description TEXT,
        url TEXT,
        status_id INTEGER,
        FOREIGN KEY(status_id) REFERENCES status(status_id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS project_skills (
        status_id INTEGER,
        project_id INTEGER,
        FOREIGN KEY(status_id) REFERENCES status(status_id),
        FOREIGN KEY(project_id) REFERENCES projects(project_id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS skills (
        skill_id INTEGER PRIMARY KEY,
        skill_name TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS status (
        status_id INTEGER PRIMARY KEY,
        status_name TEXT
    )''')

    for row in cur.execute('SELECT * FROM projects'):
        print(row)

    conn.commit()

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()