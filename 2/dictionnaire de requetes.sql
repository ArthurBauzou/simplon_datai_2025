------------------
-- TABLE SAKILA --
------------------

-- tirer un nombre aléatoire entre 1 et 200
SELECT FLOOR((RAND()*200)+1);

-- Créer une liste des fils dans lesquels a joué un acteur
SELECT f.title, a.first_name, a.last_name, a.actor_id
FROM film_actor AS fa
JOIN film AS f
ON fa.film_id = f.film_id
JOIN actor AS a
ON fa.actor_id = a.actor_id
WHERE fa.actor_id = 45;

-- Vérifier le nombre de films dans lequels ont joué un acteur
SELECT COUNT(f.title)
FROM film_actor AS fa
JOIN film AS f
ON fa.film_id = f.film_id
WHERE fa.actor_id = 6;

------------------
-- TABLE PRODU1 --
------------------

-- 1 CREATION
---------------------

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

-- 2 REQUÊTES
---------------------

-- ramener toutes les familles avec le nombre d’articles
SELECT f.nom, count(p.libelle) AS n
FROM famille AS f
JOIN produit AS p
ON f.fam_id = p.fam_id
GROUP BY f.nom
ORDER BY n DESC

-- ramener les données avec les noms de s familles et des conditionnements
SELECT p.code_art AS 'code article', 
p.libelle AS 'libellé',
f.nom AS 'famille article',
c.nom AS 'type emballage',
p.prix AS 'prix unitaire HT'
FROM produit AS p
JOIN famille AS f ON p.fam_id = f.fam_id
JOIN condit AS c ON p.cond_id = c.cond_id;

-- créer la vue correspondante afin de gagner du temps
CREATE VIEW select_all AS
SELECT p.code_art AS 'code article', 
p.libelle AS 'libellé',
f.nom AS 'famille article',
c.nom AS 'type emballage',
p.prix AS 'prix unitaire HT'
FROM produit AS p
JOIN famille AS f ON p.fam_id = f.fam_id
JOIN condit AS c ON p.cond_id = c.cond_id;

------------------
-- TABLE SALES01 --
------------------

-- 1 CREATION
---------------------

-- créer la table des catégories
CREATE TABLE category (
    cat_id UNSIGNED TINYINT PRIMARY KEY,
    name VARCHAR(30) NOT NULL UNIQUE
)

-- créer la table des sous-categories
CREATE TABLE sub_category (
    sub_id UNSIGNED SMALLINT PRIMARY KEY,
    cat_id TINYINT NOT NULL,
    sub_category VARCHAR(30) NOT NULL,
    FOREIGN KEY (cat_id) REFERENCES category(cat_id)
)

-- créer la table des produits
CREATE TABLE product (
    prod_id UNSIGNED MEDIUMINT PRIMARY KEY,
    sub_id UNSIGNED SMALLINT NOT NULL,
    product_name VARCHAR(40) NOT NULL,
    unit_price UNSIGNED MEDIUMINT,
    unit_cost UNSIGNED MEDIUMINT,
    FOREIGN KEY (sub_id) REFERENCES sub_category(sub_id)
)

-- créer la table des pays
CREATE TABLE country (
    co_id UNSIGNED SMALLINT PRIMARY KEY,
    country_name VARCHAR(30) NOT NULL UNIQUE
)

-- créer la table des régions
CREATE TABLE region (
    reg_id UNSIGNED SMALLINT PRIMARY KEY,
    co_id UNSIGNED SMALLINT,
    region_name VARCHAR(30) NOT NULL UNIQUE,
    FOREIGN KEY (co_id) REFERENCES country(co_id)
)

-- créer la table des clients
CREATE TABLE customer (
    cust_id UNSIGNED INT PRIMARY KEY,
    reg_id UNSIGNED SMALLINT,
    fisrt_name VARCHAR(30),
    last_name VARCHAR(30),
    age UNSIGNED TINYINT,
    genre VARCHAR(1),
    FOREIGN KEY (reg_id) REFERENCES region(reg_id)
)

-- créer la table des ventes
CREATE TABLE sales (
    sale_id UNSIGNED INT PRIMARY KEY AUTO_INCREMENT,
    cust_id UNSIGNED INT,
    prod_id UNSIGNED MEDIUMINT,
    sale_date DATE NOT NULL,
    quantity UNSIGNED SMALLINT,
    revenue UNSIGNED INT,
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
    FOREIGN KEY (prod_id) REFERENCES product(prod_id)
)
