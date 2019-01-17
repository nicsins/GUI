# Python code to demonstrate table creation and
# insertions with SQL

# importing module
import sqlite3

# connecting to the database
connection = sqlite3.connect("PennBroDB.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE WorkLog ( 
OrderIndex INTEGER PRIMARY KEY AUTOINCREMENT,
Date DATE , 
Location VARCHAR(20), 
Apartment VARCHAR(30), 
Description VARCHAR (100), 
Hours DOUBLE );"""

# execute the statement
crsr.execute(sql_command)

# SQL command to insert the data in the table
sql_command = """INSERT INTO WorkLog VALUES (0,1/1/2019,"Warehouse","boiler","check on leaky boiler",    1.0);"""
crsr.execute(sql_command)

# another SQL command to insert the data in the table
sql_command = """INSERT INTO WorkLog VALUES (1,1/2/2019,"Warehouse","boiler","replace 3 water heaters",9.0);"""
crsr.execute(sql_command)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# close the connection
connection.close()
