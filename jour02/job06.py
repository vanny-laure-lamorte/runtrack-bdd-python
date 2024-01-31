import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "XXX",
    database = "LaPlateforme",
)

cursor = bdd.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")
capacite_totale = cursor.fetchone()[0]

print(f'La capacite de toutes les salles est de :{capacite_totale}')

cursor.close()
bdd.close()