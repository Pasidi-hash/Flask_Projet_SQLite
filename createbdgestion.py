import sqlite3

# 1. Création automatique du fichier
conn = sqlite3.connect('gestion_taches.db')
cursor = conn.cursor()

# 2. Création de la structure demandée par le projet
cursor.execute('''
    CREATE TABLE IF NOT EXISTS taches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT NOT NULL,
        dateEcheance TEXT NOT NULL,
        statut INTEGER DEFAULT 0
    )
''')

# 3. Validation et fermeture (TRÈS IMPORTANT)
conn.commit() 
conn.close()
print("Le fichier gestion_taches.db a été généré avec la table 'taches'.")
