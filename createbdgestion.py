import sqlite3
import os

# Récupère le chemin du dossier actuel pour Alwaysdata
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "gestion_taches.db")

def init_db():
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    # [cite_start]Structure conforme au cahier des charges [cite: 1]
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS taches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT NOT NULL,
            date_echeance TEXT NOT NULL,
            statut INTEGER DEFAULT 0
        )
    ''')
    connection.commit()
    connection.close()
    print(f"Base créée à : {db_path}")

if __name__ == "__main__":
    init_db()
