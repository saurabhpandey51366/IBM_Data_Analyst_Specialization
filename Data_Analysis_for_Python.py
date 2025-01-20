#Writing Code using DB API

from dmodule import connect

#Create connection object
connection = connect('Databasename', 'username', 'pswd')

#Create a cursor object
cursor = connection.cursor()

#Run queries
cursor.execute('select * from mytable')
results = cursor.fetchall()

#Free resources
cursor.close()
connection.close()
