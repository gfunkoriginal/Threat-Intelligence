#Call the National Vulnerability Database to collect the zip file
#Extract the xml document from the zipfile
#Read the xml file and parse for the values, then place these values into the datbase

# Code for extracting xml was taken from: http://stackoverflow.com/questions/3451111/unzipping-files-in-python

import sqlite3
import urllib
import xml.etree.ElementTree as ET
import zipfile


conn = sqlite3.connect('vulncoll.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Vulnerabilities''')

cur.execute('''
CREATE TABLE Phishing_Campaigns (Url TEXT, Country TEXT, Target TEXT, Phishtank_submission TEXT, Verification_time TEXT)''')

fhand =("nvdcve-2.0-2016.xml.zip") #https://nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2016.xml.zip
print fhand.getcode()
if (fhand.getcode() == 200):
    zip_ref = zipfile.ZipFile(fhand, 'r')
    zip_ref.extractall("C:\Users\graeme.mcgibbney\workspace\ThreatIntel\Vuln")
    zip_ref.close()
    fhand = ("nvdcve-2.0-2016.xml")
    data = fhand.read()
else:
    print 'Received an error from server, cannot retrieve results ' + str(fhand.getcode())

tree = ET.fromstring(data)
    

