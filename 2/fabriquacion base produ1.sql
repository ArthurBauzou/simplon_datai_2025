-- créer la table des produits : 
CREATE TABLE IF NOT EXISTS produit (
    prod_id INT NOT NULL AUTO_INCREMENT,
    fam_id INT,
    cond_id INT,
    code INT,
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

-- ajouter des clefs étrangères à la table principale : 
ALTER TABLE  produit
ADD CONSTRAINT FOREIGN KEY (fam_id)
REFERENCES famille (fam_id)
ON UPDATE CASCADE
ON DELETE CASCADE;