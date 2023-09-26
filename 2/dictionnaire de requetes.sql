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

