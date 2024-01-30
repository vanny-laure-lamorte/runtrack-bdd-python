import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "VannyLamorte25!",
    database = "LaPlateforme",
)

cursor = bdd.cursor()
cursor.execute("SELECT * FROM etudiant")
result = cursor.fetchall()
print(result)