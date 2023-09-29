-- tables pour le fichier commandes*

-- TABLE PAYS
CREATE TABLE Pays (
    id SMALLINT PRIMARY KEY,
    nom VARCHAR(40)
)

CREATE TABLE Ville (
    id MEDIUMINT PRIMARY KEY,
    id_pays SMALLINT,
    nom VARCHAR(40),
    code_postal MEDIUMINT,
    FOREIGN KEY (id_pays) REFERENCES Pays(id)
)

CREATE TABLE Client (
    id INT PRIMARY KEY,
    id_ville MEDIUMINT,
    nom VARCHAR(30),
    prenom VARCHAR(30),
    adresse VARCHAR(80),
    email VARCHAR(50),
    FOREIGN KEY (id_ville) REFERENCES Villes(id)
)

CREATE TABLE Magasin (
    id MEDIUMINT PRIMARY KEY,
    id_ville MEDIUMINT,
    adresse VARCHAR(80),
    FOREIGN KEY (id_ville) REFERENCES Ville(id)
)

CREATE TABLE Categorie (
    id SMALLINT PRIMARY KEY,
    nom VARCHAR(40)
)

CREATE TABLE Produit (
    id INT PRIMARY KEY,
    id_cat SMALLINT,
    nom VARCHAR(80),
    prix MEDIUMINT,
    FOREIGN KEY (id_cat) REFERENCES Categorie(id)
)

CREATE TABLE Commande (
    id INT PRIMARY KEY,
    id_client INT,
    id_magasin MEDIUMINT,
    date_com DATE,
    FOREIGN KEY (id_client) REFERENCES Client(id),
    FOREIGN KEY (id_magasin) REFERENCES Magasin(id)
)

CREATE TABLE Achat (
    id_prod INT,
    id_com INT,
    PRIMARY KEY (id_prod, id_com),
    FOREIGN KEY (id_prod) REFERENCES Produit(id),
    FOREIGN KEY (id_com) REFERENCES Commande(id)
)