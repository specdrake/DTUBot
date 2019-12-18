import requests
from bs4 import BeautifulSoup

url = "http://dtu.ac.in"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
#with open("dtu2.html", "w") as fi:
#    fi.write(soup.prettify())
#    fi.close()
#html = open("dtu2.html", "r").read()
#soup = BeautifulSoup(html, 'html5lib')
links = soup.find_all(id='tab4')[0].find_all('a')
file = open('tlnk.txt', 'w')
for link in links:
    if 'href' in link.attrs:
        s = link['href']
        if s.startswith('.'):
            s = s.replace('.', 'http://www.dtu.ac.in', 1)        
        if not s.startswith('http'):
            continue
        file.write(link.string.strip() + '\n')
        file.write(s)
        file.write('\n\n')

marqs = soup.find_all('marquee')
lm = []
mfile = open('mlnk.txt', 'w')
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
            mfile.write(a.string.strip() + '\n')
            mfile.write(s)
            mfile.write('\n\n')
