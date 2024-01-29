SELECT nom, prenom, age, email
FROM etudiant
WHERE age = (SELECT MIN(age) FROM etudiant);