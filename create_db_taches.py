import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'gestion_taches.db')

# Création/Connexion au fichier .db
connection = sqlite3.connect(db_path)

# Création de la table avec les champs du PDF 
connection.execute('''
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT NOT NULL,
        dateEcheance TEXT NOT NULL,
        statut INTEGER DEFAULT 0
    )
''')

# Insertion d'exemple pour tester la liste [cite: 13]
cur = connection.cursor()
cur.execute("INSERT INTO taches (titre, description, dateEcheance) VALUES (?, ?, ?)",
            ('Test Alwaysdata', 'Vérifier l affichage de la liste', '2024-12-31'))

connection.commit()
connection.close()
print(f"Base de données initialisée à : {db_path}")
