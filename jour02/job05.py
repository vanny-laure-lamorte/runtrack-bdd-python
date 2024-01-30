import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "XXX",
    database = "LaPlateforme",
)

cursor = bdd.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")
superficie_totale = cursor.fetchone()[0]

print(f'La superficie de La Plateforme est de {superficie_totale}m2')

cursor.close()
