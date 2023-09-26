-- créer la table des produits : 
CREATE TABLE IF NOT EXISTS produit (
    prod_id INT,
    fam_id INT,
    cond_id INT,
    libelle VARCHAR(80) NOT NULL UNIQUE,
    prix DECIMAL(6,2) NOT NULL,
    PRIMARY KEY (prod_id)
)

-- créer la table des familles :
CREATE TABLE IF NOT EXISTS famille (
    fam_id INT,
    nom VARCHAR(80) NOT NULL UNIQUE,
    PRIMARY KEY (fam_id)
)

-- créer la table des conditionnements :
CREATE TABLE IF NOT EXISTS condition (
    cond_id INT,
    nom VARCHAR(80) NOT NULL UNIQUE,
    PRIMARY KEY (cond_id)
)