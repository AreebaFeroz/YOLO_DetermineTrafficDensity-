import sqlite3
import datetime

db= sqlite3.connect("database.db")
c=db.cursor()
db.row_factory = lambda c, row: row[0]


def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS roads(roadID INT PRIMARY KEY, roadName INT)')
    c.execute('CREATE TABLE IF NOT EXISTS areas(areaID INT PRIMARY KEY, areaName Text)')
    c.execute('CREATE TABLE IF NOT EXISTS density(ID INTEGER PRIMARY KEY AUTOINCREMENT, areaID INT, roadID INT, '
              'count INT,rec_time TIMESTAMP, density REAL, congestion REAL, greenDur INT, '
              'trafficFlow REAL, FOREIGN KEY(areaID) REFERENCES areas(areaID),'
              'FOREIGN KEY(roadID) REFERENCES roads(roadID))')
    c.execute('CREATE TABLE IF NOT EXISTS heaviestFlow(ID INTEGER PRIMARY KEY AUTOINCREMENT, areaID INT, roadID INT,'
              'dur INT, trafficFlow REAL, FOREIGN KEY(areaID) REFERENCES areas(areaID),'
              ' FOREIGN KEY(roadID) REFERENCES roads(roadID))')

def queryDatabase():
    # Print year and date of current date with unusual syntax
    c.execute('SELECT strftime("%Y %d","now")')
    print(c.fetchall())

    # Print year and date of current date without comma in the end
    c.execute('SELECT strftime("%Y %d","now")')
    result=[row[0] for row in c.fetchall()]
    print(result)

    #Print only dates in database
    c.execute('SELECT date(rec_time) FROM density')
    print(c.fetchall())


    #retrieve dates after specific date
    anyDate='2018-05-31'
    c.execute('SELECT date(rec_time) FROM density WHERE date(rec_time)> ?',(anyDate,))
    aftrDates=[row[0] for row in c.fetchall()]
    print("records after 2015-05-31: " + str(aftrDates))

def dataEntry():
    c.execute("INSERT INTO roads ('roadID', 'roadName') VALUES(0, 'Rd_1'),(1, 'Rd_2'),(2, 'Rd_3'), (3, 'Rd_4')")
    c.execute("INSERT INTO areas ('areaID', 'areaName') VALUES(1, 'Nazimabad'),(2, 'Gulshan'),(3, 'Gulistan-e-Jauhar'), (4, 'Nipa')")
    db.commit()

c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='roads'")
datatable = [row[0] for row in c.fetchall()]
if datatable==[]:
    createTable()
    dataEntry()
else:
    print("Database is already created. Records exists")


c.close()
db.close()









#c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='roads'")
# data=c.fetchall()
# if data==None:
#     print("its  empty")
#     print(c.fetchall())
# else:
#     print("Its not emptty")
#     print(c.fetchall())


#for row in rows:
 #   print(row)


# if (rows==0):
#     createTable()
#     dataEntry()
# else:
#     print("Table already exists")


