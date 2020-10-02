import requests
from bs4 import BeautifulSoup
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "hello"
  
for j in search(query, tld="co.in", num=10, stop=5, pause=1): 
    print(j) 
    print(type(j))
