import sqlite3

def init_db():
    conn = sqlite3.connect('gestion_taches.db')
    cursor = conn.cursor()
    # Création de la table avec les champs exigés par le doc
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS taches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT NOT NULL,
            dateEcheance TEXT NOT NULL,
            statut INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
    print("Base 'gestion_taches.db' créée avec succès !")

if __name__ == "__main__":
    init_db()
