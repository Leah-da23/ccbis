import csv
import pyodbc

server = 'da-trainingql.database.windows.net'
database = 'da-trainingql'
username = 'da-trainingql'
password = '1qaz2wsxDa'
driver = '{ODBC Driver 17 for SQL Server}'

filename = 'DimAgent.csv'   
delimiter = ','

cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433')

cursor = cnxn.cursor()
with open(DimAgent.csv, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=delimiter, quotechar='')
    for row in reader:
    
        query = "INSERT INTO dbo.AgentSource (AgentID, FirstName, LastName) VALUE"
        cursor.execute(query)
cnxn.commit()
cnxn.close()
print('test')

#  add a comment