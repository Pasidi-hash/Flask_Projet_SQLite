from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)#m                                                                                                               
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/fiche_nom')
def fiche_nom():
    # Récupère le nom depuis l'URL (?nom=DUPONT)
    nom_saisi = request.args.get('nom', '')
    
    # Connexion à la base
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    # Recherche (on utilise UPPER pour éviter les problèmes de majuscules)
    client = conn.execute("SELECT * FROM clients WHERE nom = ?", (nom_saisi,)).fetchone()
    conn.close()
    
    # On renvoie vers votre fichier
    return render_template('recherche_client.html', client=client, nom_recherche=nom_saisi)


app = Flask(__name__)
app.secret_key = 'une_cle_secrete_au_choix' # Obligatoire pour utiliser les sessions

# Route pour la recherche (protégée)
@app.route('/fiche_nom')
def fiche_nom():
    # Vérification : l'utilisateur est-il connecté ?
    if not session.get('logged_in'):
        return "Accès refusé. Veuillez vous connecter.", 401

    nom_saisi = request.args.get('nom', '')
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    client = conn.execute("SELECT * FROM clients WHERE nom = ?", (nom_saisi,)).fetchone()
    conn.close()
    
    return render_template('recherche_client.html', client=client, nom_recherche=nom_saisi)

# 1. Vérification des identifiants demandés (Exercice 2)
def verifier_auth(username, password):
    return username == 'user' and password == '12345'

# 2. Fonction qui déclenche la fenêtre de "Pop-up" dans le navigateur
def demander_identification():
    return Response(
        'Veuillez vous connecter avec user / 12345', 401,
        {'WWW-Authenticate': 'Basic realm="Acces Fiche Client"'}
    )

@app.route('/fiche_nom/')
def fiche_nom():
    # 3. On regarde si l'utilisateur a rempli la fenêtre d'identification
    auth = request.authorization
    
    if not auth or not verifier_auth(auth.username, auth.password):
        # Si non, ou si c'est faux, on fait apparaître/réapparaître le pop-up
        return demander_identification()

    # 4. Si l'identification est réussie, on exécute la recherche
    nom_saisi = request.args.get('nom', '')
    
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    
    client_trouve = conn.execute("SELECT * FROM clients WHERE nom = ?", (nom_saisi,)).fetchone()
    conn.close()
    
    # 5. On affiche votre fichier HTML avec les résultats
    return render_template('recherche_client.html', client=client_trouve, nom_recherche=nom_saisi)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')  # afficher le formulaire

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement
                                                                                                                                       
if __name__ == "__main__":
  app.run(debug=True)
