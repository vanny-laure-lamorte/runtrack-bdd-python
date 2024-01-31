import mysql.connector

class ZooManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def ajout_animal(self, nom, race, id_type_cage, date_naissance, pays_origine):
        sql = "INSERT INTO animal (nom, race, id_type_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_type_cage, date_naissance, pays_origine)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def supprimer_animal(self, animal_id):
        sql = "DELETE FROM animal WHERE id = %s"
        values = (animal_id)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def modifer_animal(self, animal_id, new_values):
        set_clause = ", ".join([f"{key} = '{value}'" for key, value in new_values.items()])
        sql = f"UPDATE animal SET {set_clause} WHERE id = %s"
        self.cursor.execute(sql, (animal_id,))
        self.connection.commit()

    def display_animals(self):
        sql = "SELECT * FROM animal"
        self.cursor.execute(sql)
        animals = self.cursor.fetchall()
        for animal in animals:
            print(animal)
            
    def display_cage(self):
        sql = "SELECT * FROM cage"
        self.cursor.execute(sql)
        cages = self.cursor.fetchall()
        for cage in cages:
            print(cage)

    def display_animals_in_cages(self):
        sql = "SELECT cage.id, cage.superficie, cage.capacite FROM cage LEFT JOIN animal ON cage.id = animal.id_type_cage"
        self.cursor.execute(sql)
        animals_in_cages = self.cursor.fetchall()
        print("Il y a ",len(animals_in_cages)," animaux dans la cage")
        
    def calculate_total_cage_area(self):
        sql = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(sql)
        total_area = self.cursor.fetchone()[0]
        print(f"La superficie totale de toutes les cages est de : {total_area} m²")
        
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

zoo_manager = ZooManager("localhost", "root", "XXX", "Zoo")

# zoo_manager.ajout_animal("Serpent", "Anaconda", 1, "2021-10-15", "Asie")

# zoo_manager.modifer_animal(1, {'nom': 'Lion King'})

# zoo_manager.supprimer_animal(2)

# zoo_manager.display_animals()
# zoo_manager.display_cage()

zoo_manager.display_animals_in_cages()
zoo_manager.calculate_total_cage_area()
zoo_manager.close_connection()