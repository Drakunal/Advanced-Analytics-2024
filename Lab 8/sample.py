import mysql.connector

# Establishing a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=" retail_store_genai"
)

# Creating a cursor object
mycursor = mydb.cursor()

# Execute SELECT query
mycursor.execute("SELECT * FROM products")

# Fetching all rows
result = mycursor.fetchall()

# Printing the results
for row in result:
    print(row)

# Closing the connection
mydb.close()
