DROP TABLE IF EXISTS taches;

CREATE TABLE taches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,          -- Correspond à name="titre"
    description TEXT NOT NULL,    -- Correspond à name="description"
    date_echeance TEXT NOT NULL,  -- Correspond à name="dateEcheance"
    statut INTEGER DEFAULT 0      -- 0 = En cours, 1 = Terminé
);
