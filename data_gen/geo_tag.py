import re
import sys
from pyzipcode import ZipCodeDatabase
import reverse_geocoder as rg
import random
import string

flist=str(sys.argv)
tfile= flist[12:len(flist)-2]
#f = open(tfile, 'r')
f = open("sent9.txt", 'r')
g = open("t9.txt", 'w')

zcdb = ZipCodeDatabase()
c=0
for line in f:
    fcoords=()
    tweet = line.split("|")
    coords = re.search(r"\[(.*)\]", tweet[0]).group(1)
    x, y = map(float, re.findall(r'[+-]?[0-9.]+', coords))
    location = rg.search([x,y])
    if location[0]['cc'] == "US":
        state = location[0]['admin1']
        city = location[0]['name']
        zlist=zcdb.find_zip(city=city)
        if zlist>0:
            zipcode = random.choice(zlist)
            s = tweet[-1].strip('\n')+","+zipcode.zip+","+state+"\n"
#    print s.encode("UTF-8")
            g.write(s.encode('utf8'))
    c+=1
    if c>100:
        g.flush()
        c=0
f.close()
g.close()
