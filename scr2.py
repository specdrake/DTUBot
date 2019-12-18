import requests
from bs4 import BeautifulSoup

url = "http://dtu.ac.in"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
links = soup.find_all(id='tab4')[0].find_all('a')
tfup = open('tfup.txt', 'w')
mfup = open('mfup.txt', 'w')
ot = ""
om = ""
with open('tlnk.txt', 'r') as t1:
    ot = t1.read()
    t1.close()
with open('mlnk.txt', 'r') as t2:
    om = t2.read()
    t2.close()
otf = open('tlnk.txt', 'w')
omf = open('mlnk.txt', 'w')
for link in links:
    if 'href' in link.attrs:
        s = link['href']
        if s.startswith('.'):
            s = s.replace('.', 'http://www.dtu.ac.in', 1)        
        if not s.startswith('http'):
            continue
        if s not in ot:
            tfup.write(link.string.strip() + '\n')
            tfup.write(s)
            tfup.write('\n\n')
        
        otf.write(link.string.strip() + '\n')
        otf.write(s)
        otf.write('\n\n')
            

marqs = soup.find_all('marquee')
lm = []
for marq in marqs:
    lm.append(marq.find_all('a'))
for l in lm:
    for a in l:
        if 'href' in a.attrs:
            s = a['href']
            if s.startswith('.'):
                s = s.replace('.', 'http://www.dtu.ac.in', 1)
            if not s.startswith('http'):
                continue
            if s not in om:
                mfup.write(a.string.strip() + '\n')
                mfup.write(s)
                mfup.write('\n\n')
                
            omf.write(a.string.strip() + '\n')
            omf.write(s)
            omf.write('\n\n')
