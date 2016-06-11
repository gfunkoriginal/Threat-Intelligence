import sqlite3
import urllib
import json
import sys

fhand = urllib.urlopen('http://isc.sans.edu/api/getmspatchday/2016-03-08?json')

print fhand.getcode()

data = fhand.read()

js = json.loads(data)

threatlist = []
count = 0
for record in js["getmspatchday"]:
    threat = record["affected"]
    threatlist.insert(count, threat)
    count = count + 1


try:
    conn = sqlite3.connect('asset_base2.sqlite')
    cur = conn.cursor()
except:
    print "error"
for threat in threatlist:
    result = cur.execute('''
    SELECT * FROM * WHERE InstalledApplications = (?)''', threat)
    print result

print json.dumps(js, indent = 4)


