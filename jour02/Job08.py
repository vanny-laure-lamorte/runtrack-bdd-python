"""

CREATE DATABASE Zoo;
SHOW Databases;

USE Zoo;

CREATE TABLE animal(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    race VARCHAR(255),
    id_type_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(255) 
    );

SHOW COLUMNS
FROM employe;

INSERT INTO employe(nom,prenom,salaire,id_service) VALUES
('Lorquet', 'Ines', 3800, 1),
('Madec','Lucy', 4000, 2),
('Iribaren','Lucas', 4800, 3),
('Martinie','Lucas', 5000, 4),
('Cordial', 'Alicia', 6000, 5);

SELECT *
FROM employe;

CREATE TABLE service (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
    ); 

SHOW COLUMNS
FROM service;

INSERT INTO service(nom) VALUES
('technicien de surface'),
('Assistant Administratif'), 
('Accompagnateur'),
('Responsable Pedagogique'), 
('Directeur'); 

SELECT *
FROM service; 

SELECT employe.nom, employe.prenom, employe.salaire, service.nom as service
FROM employe
JOIN service ON employe.id_service = service.id

"""

class Salaire: 

    def __init__(self):
        pass