#Collect the data, strip it to get just the domain
import sqlite3
import urllib

conn = sqlite3.connect('dnscoll.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Collect''')

cur.execute('''
CREATE TABLE Collect (domain TEXT)''')


count = 0
fhand = urllib.urlopen('http://malwaredomains.lehigh.edu/files/justdomains')
for line in fhand:
    #print line.strip()
    count = count + 1
    cur.execute('''INSERT INTO Collect (domain) VALUES (?) ''', (line, ))

conn.commit()
print count
