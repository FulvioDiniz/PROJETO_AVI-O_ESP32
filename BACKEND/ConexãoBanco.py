import mysql.connector

host = "localhost"
user = "root"
password = ""
database = "sensor_db"


mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM dht11")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)




def insert_data(data):
    sql = "INSERT INTO dht11 (temperatura, umidade) VALUES (%s, %s)"
    val = (data[0], data[1])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def select_data():
    mycursor.execute("SELECT * FROM dht11")
    myresult = mycursor.fetchall()
    return myresult

def delete_data():
    sql = "DELETE FROM dht11 WHERE temperatura = 0"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def update_data():
    sql = "UPDATE dht11 SET temperatura = 0 WHERE temperatura = 0"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")


def selecionar_temperatura():
    mycursor.execute("SELECT temperatura FROM dht11")
    myresult = mycursor.fetchall()
    return myresult

def selecionar_umidade():
    mycursor.execute("SELECT umidade FROM dht11")
    myresult = mycursor.fetchall()
    return myresult

