import sqlite3

# Connexion à la nouvelle base de données
connection = sqlite3.connect('gestion_taches.db')

# Lecture et exécution du schéma
with open('schema_taches.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion d'une tâche d'exemple (optionnel)
cur.execute("INSERT INTO taches (titre, description, date_echeance) VALUES (?, ?, ?)",
            ('Projet IT', 'Créer l application web simple', '2024-05-20'))

connection.commit()
connection.close()

print("La base de données 'gestion_taches.db' a été créée avec succès.")
