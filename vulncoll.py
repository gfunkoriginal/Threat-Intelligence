#Call the National Vulnerability Database to collect the zip file
#Extract the xml document from the zipfile
#Read the xml file and parse for the values, then place these values into the datbase

# Code for extracting xml was taken from: http://stackoverflow.com/questions/3451111/unzipping-files-in-python

import sqlite3
import urllib
import xml
import zipfile


conn = sqlite3.connect('phishcoll.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Collect''')

cur.execute('''
CREATE TABLE Collect (domain TEXT)''')

fhand =("nvdcve-2.0-2016.xml.zip") #https://nvd.nist.gov/feeds/xml/cve/nvdcve-2.0-2016.xml.zip

zip_ref = zipfile.ZipFile(fhand, 'r')
zip_ref.extractall("C:\Users\graeme.mcgibbney\workspace\ThreatIntel\Vuln")
zip_ref.close()

print "done"



#fzip = ZipFile.getinfo(fhand)

#print fzip
    

