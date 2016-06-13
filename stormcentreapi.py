import sqlite3
import urllib
import json
import sys

fHand = urllib.urlopen('http://isc.sans.edu/api/getmspatchday/2016-01-12?json')

print fHand.getcode()

data = fHand.read()

js = json.loads(data)

print json.dumps(js, indent=4)


threatList = []
count = 0
for record in js["getmspatchday"]:
    threat = record["affected"]
    threatList.insert(count, threat)
    ++count

print threatList
try:
    conn = sqlite3.connect('asset_base2.sqlite')
    cur = conn.cursor()
except:
    print "error"

for threat in threatList:
    result = cur.execute('SELECT * FROM database_servers WHERE InstalledApplications Like (%?%)', (threat, ))
    print result

#print json.dumps(js, indent = 4)

