import sqlite3
import urllib
import json
import sys

#The ambition is to have the date automatically updated to the second tuesday of every month.
# Thereby running without needing manually amend the date.
#Run as a Cron job that will pull out today's date and insert this into the date of the urllib call.
fHand = urllib.urlopen('http://isc.sans.edu/api/getmspatchday/2016-01-12?json')

print fHand.getcode()

data = fHand.read()

js = json.loads(data)

print json.dumps(js, indent=4)

threatList = []
count = 0

#To do, we wish to pull out the criticality of the patch as well as the system affected
for record in js["getmspatchday"]:
    threat = record["affected"]
    threatList.insert(count, threat)
    ++count

#print threatList
try:
    conn = sqlite3.connect('asset_base2.sqlite')
    cur = conn.cursor()
except:
    print "error"
# Need to create another data structure which results can be appended to.
# This will enable us to undex the results in a batch oriented fashion.
for threat in threatList:
    result = cur.execute("SELECT * FROM database_servers WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM email_servers WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM dev_servers WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM domain_controllers WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM exchange WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM file_transfer WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM huxley WHERE InstalledApplications='%s' UNION ALL "
                         "SELECT * FROM pas WHERE InstalledApplications = '%s'"
                         % (threat, threat, threat, threat, threat, threat, threat, threat))
    print result.fetchall()

