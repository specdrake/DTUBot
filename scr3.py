import requests
from bs4 import BeautifulSoup

html = open("dtu.html").read()
soup = BeautifulSoup(html, 'html5lib')
links = soup.find_all(id='tab4')[0].find_all('a')
file = open('tlnk.txt', 'w')
for link in links:
    s = link['href']
    if s.startswith('.'):
        s = s.replace('.', 'http://www.dtu.ac.in', 1)
    if not s.startswith('http'):
        continue
    file.write(str(link.string).strip() + '\n')
    file.write(s)
    file.write('\n\n')
    
