import sqlite3
import os

# Utilisation du chemin absolu pour Alwaysdata
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'gestion_taches.db')

connection = sqlite3.connect(db_path)

# On crée la table 'taches' avec les colonnes du projet [cite: 8, 13]
connection.execute('''
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT NOT NULL,
        date_echeance TEXT NOT NULL,
        statut INTEGER DEFAULT 0
    )
''')

cur = connection.cursor()

# Insertion d'une tâche de test (comme dans votre modèle image_c913bd.png)
cur.execute("INSERT INTO taches (titre, description, date_echeance) VALUES (?, ?, ?)",
            ('Projet IT', 'Finir le déploiement sur Alwaysdata', '2024-06-01'))

connection.commit()
connection.close()

print(f"Base de données créée avec succès à l'emplacement : {db_path}")
