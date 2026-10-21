#!/usr/bin/python3

import mysql.connector

# print(mysql.connector)

#establishing the connection
conn = mysql.connector.connect(user='remoteuser', password='testerific', host='161.35.237.176', database='tester')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()


cursor.execute("SELECT * FROM employees")

data = cursor.fetchall()

print(data)

for record in data:
    print(f'His name is... {record[2]}')

# display each index value in the list
for i in range(len(data)):
    print(data[i])

#Closing the connection
conn.close()
