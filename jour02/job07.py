
import mysql.connector
class Salarie:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        
    def create_employee(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.connection.commit()
        
    def read_all_employees(self):
        sql = "SELECT * FROM employe"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_employee_salary(self, employee_id, new_salary):
        sql = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salary, employee_id)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employe WHERE id = %s"
        values = (employee_id,)
        self.cursor.execute(sql, values)
        self.connection.commit()

salarie_manager = Salarie("localhost", "root", "azerty", "LaPlateforme2")
salarie_manager.create_employee("Personne", "Test", 4500.00, 2)
# salarie_manager.read_all_employees()
salarie_manager.update_employee_salary(1, 3800.00)
# salarie_manager.read_all_employees()
# salarie_manager.delete_employee(9)
salarie_manager.read_all_employees()

"""
CREATE DATABASE Plateforme2;
SHOW Databases;

USE Plateforme2;

CREATE TABLE employe(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire FLOAT,
    id_service INT 
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