import mysql.connector

bdd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "XXX",
    database = "LaPlateforme",
)

cursor = bdd.cursor()
cursor.execute("SELECT * FROM salle")
result = cursor.fetchall()
print(result)